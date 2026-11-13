#!/usr/bin/env python3
"""Transcribe lecture page PNGs with Google Gemini vision models."""

from __future__ import annotations

import argparse
import asyncio
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from google import genai
from google.genai import types

OCR_PROMPT = """Transcribe this handwritten lecture page.

Requirements:
- Output markdown only, no preamble or commentary.
- Use LaTeX for all math: $...$ inline, $$...$$ display.
- Preserve reading order and paragraph structure.
- For hand-drawn diagrams or graphs, add a brief [diagram: description] line where the diagram appears.
- Transcribe text as faithfully as possible; use [illegible] for unclear words.
"""

# Ordered best -> minimum acceptable. Free-tier quotas are tracked per model,
# so when one model is throttled/exhausted the next one is used.
# 3.8-flash measured much slower than the rest even at LOW thinking, so it is
# tried last among the good models.
DEFAULT_MODEL_CHAIN = [
    "gemini-3.6-flash",
    "gemini-3-flash-preview",
    "gemini-3.8-flash",
    "gemini-2.5-flash",
    "gemini-3.5-flash-lite",
]
DEFAULT_CONCURRENCY = 4
DEFAULT_REQUEST_INTERVAL_SEC = 0.5
SIDECAR_SUFFIX = ".ocr.md"
STALE_TRANSCRIPTION_NOTICE = (
    "**STALE** — page image was re-rendered; transcription pending."
)
REQUEST_TIMEOUT_SEC = 60
MAX_RETRY_ATTEMPTS = 5
RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}
RETRY_DELAY_RE = re.compile(r"Please retry in ([\d.]+)s", re.IGNORECASE)
RETRY_INFO_DELAY_RE = re.compile(r"^(\d+(?:\.\d+)?)s?$")


@dataclass(frozen=True)
class RateLimitInfo:
    quota_kind: str
    quota_id: str
    limit: int | None
    model: str | None
    retry_after_sec: float | None
    message: str

    @property
    def is_daily_quota(self) -> bool:
        return "perday" in self.quota_id.lower()

    @property
    def is_minute_quota(self) -> bool:
        return "perminute" in self.quota_id.lower() or "rpm" in self.quota_id.lower()


class PageRetriesExhausted(Exception):
    def __init__(self, image_path: Path, cause: Exception) -> None:
        self.image_path = image_path
        self.cause = cause
        super().__init__(f"retries exhausted for {image_path}: {cause}")


@dataclass
class RunController:
    abort: asyncio.Event = field(default_factory=asyncio.Event)
    abort_reason: str = ""
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def abort_run(self, reason: str) -> None:
        async with self._lock:
            if self.abort.is_set():
                return
            self.abort_reason = reason
            self.abort.set()

    @property
    def aborted(self) -> bool:
        return self.abort.is_set()


@dataclass
class ModelPool:
    """Ordered model chain. Always hands out the best model that is usable now."""

    models: list[str]
    log: "Logger"
    exhausted: dict[str, str] = field(default_factory=dict)
    _cooldown_until: dict[str, float] = field(default_factory=dict)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def acquire_model(self) -> str | None:
        """Best non-exhausted, non-cooling model; waits if all are cooling.

        Returns None when every model is exhausted.
        """
        while True:
            async with self._lock:
                live = [m for m in self.models if m not in self.exhausted]
                if not live:
                    return None
                now = time.monotonic()
                for model in live:
                    if self._cooldown_until.get(model, 0.0) <= now:
                        return model
                wait = min(self._cooldown_until[m] for m in live) - now
            await asyncio.sleep(max(wait, 0.1))

    async def cool_down(self, model: str, seconds: float) -> None:
        async with self._lock:
            until = time.monotonic() + seconds
            self._cooldown_until[model] = max(
                self._cooldown_until.get(model, 0.0), until
            )

    async def exhaust(self, model: str, reason: str) -> None:
        async with self._lock:
            if model in self.exhausted:
                return
            self.exhausted[model] = reason
            remaining = [m for m in self.models if m not in self.exhausted]
        await self.log.emit_async(
            "switch",
            f"{model} unavailable ({reason}); "
            + (f"remaining: {', '.join(remaining)}" if remaining else "no models left"),
            err=True,
        )


@dataclass
class Logger:
    verbose: bool
    repo_root: Path
    started_at: float = field(default_factory=time.monotonic)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    def emit(self, level: str, message: str, *, err: bool = False) -> None:
        stream = sys.stderr if err else sys.stdout
        print(f"{level:<8} {message}", file=stream, flush=True)

    async def emit_async(self, level: str, message: str, *, err: bool = False) -> None:
        async with self._lock:
            self.emit(level, message, err=err)

    def info(self, message: str) -> None:
        self.emit("info", message)

    async def detail(self, message: str) -> None:
        if self.verbose:
            await self.emit_async("detail", message)

    def skip(self, image_path: Path, reason: str) -> None:
        relative = image_path.relative_to(self.repo_root)
        self.emit("skip", f"{relative} ({reason})")

    def pending(self, image_path: Path, reason: str) -> None:
        relative = image_path.relative_to(self.repo_root)
        if self.verbose:
            self.emit("pending", f"{relative} ({reason})")

    async def run(self, index: int, total: int, image_path: Path) -> None:
        relative = image_path.relative_to(self.repo_root)
        await self.emit_async("info", f"[{index}/{total}] {relative}")
        await self.detail(f"calling Gemini for {relative}")

    async def retry(
        self,
        index: int,
        total: int,
        model: str,
        delay: float,
        info: RateLimitInfo,
        attempt: int | None = None,
    ) -> None:
        attempt_text = (
            f"attempt {attempt}/{MAX_RETRY_ATTEMPTS}, " if attempt is not None else ""
        )
        await self.emit_async(
            "retry",
            f"[{index}/{total}] {model} {info.quota_kind} throttle "
            f"({attempt_text}cooldown {delay:.0f}s, "
            f"limit={info.limit or '?'})",
            err=True,
        )

    async def stop(self, reason: str, remaining: int) -> None:
        await self.emit_async(
            "stop",
            f"{reason} — aborting run, {remaining} page(s) not attempted.",
            err=True,
        )

    async def done(self, output_path: Path, char_count: int, elapsed: float) -> None:
        relative = output_path.relative_to(self.repo_root)
        await self.emit_async(
            "done", f"{relative} ({char_count} chars, {elapsed:.1f}s)"
        )

    async def fail(self, image_path: Path, exc: Exception) -> None:
        relative = image_path.relative_to(self.repo_root)
        await self.emit_async("fail", f"{relative}: {exc}", err=True)

    def summary(
        self,
        *,
        transcribed: int,
        skipped: int,
        failed: int,
        pending: int,
    ) -> None:
        elapsed = time.monotonic() - self.started_at
        self.info(
            f"summary  transcribed={transcribed} skipped={skipped} "
            f"failed={failed} pending={pending} elapsed={elapsed:.1f}s"
        )


@dataclass
class RateLimiter:
    concurrency: int
    min_interval_sec: float
    semaphore: asyncio.Semaphore = field(init=False)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    _paused_until: float = 0.0
    _last_request_at: float = 0.0

    def __post_init__(self) -> None:
        self.semaphore = asyncio.Semaphore(self.concurrency)

    async def acquire(self) -> None:
        await self.semaphore.acquire()
        try:
            async with self._lock:
                now = time.monotonic()
                if now < self._paused_until:
                    await asyncio.sleep(self._paused_until - now)
                    now = time.monotonic()
                wait = self._last_request_at + self.min_interval_sec - now
                if wait > 0:
                    await asyncio.sleep(wait)
                    now = time.monotonic()
                self._last_request_at = now
        except Exception:
            self.semaphore.release()
            raise

    def release(self) -> None:
        self.semaphore.release()

    async def pause_all(self, seconds: float) -> None:
        async with self._lock:
            self._paused_until = max(self._paused_until, time.monotonic() + seconds)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe lecture page PNGs with Google Gemini."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--lectures-dir",
        type=Path,
        default=None,
        help="Lectures directory (overrides --repo-root derived path)",
    )
    parser.add_argument(
        "--lecture",
        type=str,
        default="",
        help="Process only lectures whose folder name contains this substring",
    )
    parser.add_argument(
        "--page",
        type=str,
        default="",
        help='Page filter: "03", "page-03", or partial match',
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Use a single Gemini model id (no fallback chain)",
    )
    parser.add_argument(
        "--models",
        type=str,
        default=None,
        help=(
            "Comma-separated fallback chain, best first "
            f"(default: {','.join(DEFAULT_MODEL_CHAIN)})"
        ),
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max parallel API requests (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--request-interval",
        type=float,
        default=DEFAULT_REQUEST_INTERVAL_SEC,
        help=(
            "Minimum seconds between request starts across all workers "
            f"(default: {DEFAULT_REQUEST_INTERVAL_SEC})"
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-transcribe even when an up-to-date sidecar already exists",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List pages that would be transcribed without calling the API",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Sync mode: skip quietly without an API key; do not fail on page errors",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed progress: scan results, API calls, retries, timings",
    )
    return parser.parse_args()


def load_env(repo_root: Path) -> None:
    from dotenv import load_dotenv

    load_dotenv(repo_root / ".env")


def get_api_key(sync: bool, log: Logger) -> str | None:
    api_key = (
        os.environ.get("GOOGLE_API_KEY", "").strip()
        or os.environ.get("GEMINI_API_KEY", "").strip()
    )
    if api_key:
        log.emit("detail", "loaded API key from environment") if log.verbose else None
        return api_key

    message = (
        "GOOGLE_API_KEY is not set. Add it to .env in the repo root "
        "or export it in your shell. Get a key at "
        "https://aistudio.google.com/apikey"
    )
    if sync:
        log.info(f"ocr skipped ({message})")
        return None

    print(message, file=sys.stderr)
    sys.exit(1)


def ocr_sidecar_path(image_path: Path) -> Path:
    return image_path.with_name(f"{image_path.stem}{SIDECAR_SUFFIX}")


def format_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")


def transcription_status(
    image_path: Path,
    sidecar_path: Path,
    force: bool,
) -> tuple[bool, str]:
    if force:
        return True, "forced"
    if not sidecar_path.exists():
        return True, "missing sidecar"
    sidecar_text = sidecar_path.read_text(encoding="utf-8")
    if STALE_TRANSCRIPTION_NOTICE in sidecar_text:
        return True, "sidecar marked stale"
    if image_path.stat().st_mtime > sidecar_path.stat().st_mtime:
        return (
            True,
            "png newer than sidecar "
            f"(png {format_mtime(image_path)}, sidecar {format_mtime(sidecar_path)})",
        )
    return (
        False,
        "sidecar up-to-date "
        f"(png {format_mtime(image_path)}, sidecar {format_mtime(sidecar_path)})",
    )


def page_matches_filter(filename: str, page_filter: str) -> bool:
    if not page_filter:
        return True
    if page_filter.isdigit():
        padded = page_filter.zfill(2)
        return filename in {f"page-{page_filter}.png", f"page-{padded}.png"}
    if not page_filter.startswith("page-"):
        return page_filter in filename
    return filename == page_filter or filename == f"{page_filter}.png"


def find_lecture_page_images(
    lectures_dir: Path,
    lecture_filter: str,
    page_filter: str,
) -> list[Path]:
    images: list[Path] = []
    asset_dirs = sorted(
        (path for path in lectures_dir.iterdir() if path.is_dir()),
        key=lambda path: path.name,
        reverse=True,
    )
    for asset_dir in asset_dirs:
        if lecture_filter and lecture_filter not in asset_dir.name:
            continue
        for png in sorted(asset_dir.glob("page-*.png")):
            if page_matches_filter(png.name, page_filter):
                images.append(png)
    return images


def write_transcription_sidecar(
    image_path: Path,
    text: str,
    model: str,
) -> Path:
    output_path = ocr_sidecar_path(image_path)
    page_name = image_path.stem
    lecture_name = image_path.parent.name
    body = text.strip() if text.strip() else "*(empty response)*"

    markdown = "\n".join(
        [
            f"# {lecture_name} - {page_name}",
            "",
            f"> Gemini {model} transcription.",
            "",
            body,
            "",
        ]
    )
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def create_client(api_key: str, log: Logger) -> genai.Client:
    if log.verbose:
        log.emit(
            "detail",
            f"creating Gemini client (timeout {REQUEST_TIMEOUT_SEC}s, "
            "app-level retries enabled)",
        )
    return genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            timeout=REQUEST_TIMEOUT_SEC * 1000,
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )


def thinking_config_for(model: str) -> types.ThinkingConfig | None:
    """OCR needs little reasoning; keep thinking minimal to cut latency.

    Gemini 2.5 uses a token budget, Gemini 3.x uses a level.
    """
    if model.startswith("gemini-2.5"):
        return types.ThinkingConfig(thinking_budget=0)
    return types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW)


def resolve_model_chain(args: argparse.Namespace) -> list[str]:
    if args.models:
        chain = [m.strip() for m in args.models.split(",") if m.strip()]
        if chain:
            return chain
    if args.model:
        return [args.model.strip()]
    return list(DEFAULT_MODEL_CHAIN)


def is_model_not_found_error(exc: Exception) -> bool:
    from google.genai import errors

    return isinstance(exc, errors.APIError) and exc.code == 404


def is_retryable_error(exc: Exception) -> bool:
    from google.genai import errors

    if isinstance(exc, errors.APIError):
        return exc.code in RETRYABLE_STATUS_CODES
    return isinstance(exc, (TimeoutError, ConnectionError, OSError))


def _parse_retry_delay_value(value: str | None) -> float | None:
    if not value:
        return None
    match = RETRY_INFO_DELAY_RE.match(value.strip())
    if not match:
        return None
    return float(match.group(1))


def _iter_error_details(exc: Exception) -> list[object]:
    from google.genai import errors

    if not isinstance(exc, errors.APIError):
        return []

    payload = exc.details
    if isinstance(payload, dict):
        error = payload.get("error", payload)
        if isinstance(error, dict):
            details = error.get("details", [])
            if isinstance(details, list):
                return details
    return []


def parse_rate_limit_error(exc: Exception) -> RateLimitInfo | None:
    from google.genai import errors

    if not isinstance(exc, errors.APIError) or exc.code != 429:
        return None

    quota_kind = "unknown"
    quota_id = ""
    limit: int | None = None
    model: str | None = None
    retry_after_sec: float | None = None
    message = exc.message or str(exc)

    for detail in _iter_error_details(exc):
        if not isinstance(detail, dict):
            continue
        detail_type = detail.get("@type", "")
        if detail_type.endswith("QuotaFailure"):
            violations = detail.get("violations", [])
            if not isinstance(violations, list):
                continue
            for violation in violations:
                if not isinstance(violation, dict):
                    continue
                quota_id = str(violation.get("quotaId", quota_id))
                quota_value = violation.get("quotaValue")
                if quota_value is not None:
                    limit = int(quota_value)
                dimensions = violation.get("quotaDimensions", {})
                if isinstance(dimensions, dict):
                    model = dimensions.get("model", model)
                if "perday" in quota_id.lower():
                    quota_kind = "daily"
                elif "perminute" in quota_id.lower():
                    quota_kind = "per-minute"
        if detail_type.endswith("RetryInfo"):
            retry_after_sec = _parse_retry_delay_value(detail.get("retryDelay"))

    match = RETRY_DELAY_RE.search(message)
    if match:
        retry_after_sec = float(match.group(1))

    if not quota_id and not retry_after_sec:
        return None

    return RateLimitInfo(
        quota_kind=quota_kind,
        quota_id=quota_id,
        limit=limit,
        model=model,
        retry_after_sec=retry_after_sec,
        message=message,
    )


def retry_delay_seconds(info: RateLimitInfo, attempt: int) -> float:
    if info.retry_after_sec is not None:
        return info.retry_after_sec + 1.0
    if info.is_minute_quota:
        return min(60.0, 5.0 * attempt)
    return min(60.0, 2.0 * (2 ** (attempt - 1)))


async def transcribe_image(
    client: genai.Client,
    image_path: Path,
    pool: ModelPool,
    log: Logger,
    index: int,
    total: int,
    limiter: RateLimiter,
    controller: RunController,
) -> tuple[str, str]:
    """Transcribe one page, falling back through the model chain on quota errors.

    Returns (text, model_used).
    """
    image_bytes = await asyncio.to_thread(image_path.read_bytes)
    await log.detail(f"read {len(image_bytes)} bytes from {image_path.name}")
    last_error: Exception | None = None
    transient_failures = 0
    rate_limit_hits = 0
    max_rate_limit_hits = 4 * len(pool.models)

    while True:
        if controller.aborted:
            raise PageRetriesExhausted(image_path, RuntimeError("run aborted"))
        model = await pool.acquire_model()
        if model is None:
            reasons = "; ".join(f"{m}: {r}" for m, r in pool.exhausted.items())
            raise PageRetriesExhausted(
                image_path,
                RuntimeError(f"all models exhausted ({reasons})"),
            )
        await limiter.acquire()
        try:
            await log.detail(f"api request using {model}")
            response = await client.aio.models.generate_content(
                model=model,
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    OCR_PROMPT,
                ],
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    thinking_config=thinking_config_for(model),
                ),
            )
            if not response.text:
                raise RuntimeError("Gemini returned an empty response")
            await log.detail(f"received {len(response.text)} chars from {model}")
            return response.text, model
        except Exception as exc:
            last_error = exc
            if is_model_not_found_error(exc):
                await pool.exhaust(model, "model not found")
                continue
            if not is_retryable_error(exc):
                raise PageRetriesExhausted(image_path, exc) from exc

            rate_limit = parse_rate_limit_error(exc)
            if rate_limit is not None:
                if rate_limit.is_daily_quota:
                    await pool.exhaust(model, "daily quota")
                    continue
                rate_limit_hits += 1
                if rate_limit_hits > max_rate_limit_hits:
                    raise PageRetriesExhausted(image_path, exc) from exc
                delay = retry_delay_seconds(rate_limit, 1)
                await pool.cool_down(model, delay)
                await log.retry(index, total, model, delay, rate_limit)
                continue

            transient_failures += 1
            if transient_failures >= MAX_RETRY_ATTEMPTS:
                raise PageRetriesExhausted(image_path, exc) from exc
            transient = RateLimitInfo(
                quota_kind="transient",
                quota_id="",
                limit=None,
                model=None,
                retry_after_sec=None,
                message=str(exc),
            )
            delay = retry_delay_seconds(transient, transient_failures)
            await pool.cool_down(model, delay)
            await log.retry(
                index, total, model, delay, transient, attempt=transient_failures
            )
        finally:
            limiter.release()


async def process_page(
    client: genai.Client,
    image_path: Path,
    pool: ModelPool,
    log: Logger,
    index: int,
    total: int,
    limiter: RateLimiter,
    controller: RunController,
) -> None:
    await log.run(index, total, image_path)
    started = time.monotonic()
    text, model = await transcribe_image(
        client,
        image_path,
        pool,
        log,
        index,
        total,
        limiter,
        controller,
    )
    output_path = await asyncio.to_thread(
        write_transcription_sidecar,
        image_path,
        text,
        model,
    )
    elapsed = time.monotonic() - started
    await log.done(output_path, len(text), elapsed)


async def transcribe_pending(
    client: genai.Client,
    pending: list[Path],
    pool: ModelPool,
    log: Logger,
    limiter: RateLimiter,
    concurrency: int,
) -> tuple[int, int, int]:
    controller = RunController()
    work_queue: asyncio.Queue[tuple[int, Path] | None] = asyncio.Queue()
    for index, image_path in enumerate(pending, start=1):
        work_queue.put_nowait((index, image_path))

    transcribed = 0
    transcribed_lock = asyncio.Lock()

    async def worker() -> None:
        nonlocal transcribed
        while not controller.aborted:
            try:
                item = work_queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            if item is None:
                work_queue.task_done()
                return
            index, image_path = item
            try:
                await process_page(
                    client,
                    image_path,
                    pool,
                    log,
                    index,
                    len(pending),
                    limiter,
                    controller,
                )
                async with transcribed_lock:
                    transcribed += 1
            except PageRetriesExhausted as exc:
                await log.fail(exc.image_path, exc.cause)
                await controller.abort_run(str(exc.cause))
            finally:
                work_queue.task_done()

    workers = [asyncio.create_task(worker()) for _ in range(concurrency)]
    await asyncio.gather(*workers)

    not_attempted = len(pending) - transcribed - (1 if controller.aborted else 0)
    failed = 1 if controller.aborted else 0
    return transcribed, failed, max(not_attempted, 0)


async def async_main(
    args: argparse.Namespace,
    log: Logger,
    pending: list[Path],
    skipped: int,
) -> int:
    api_key = get_api_key(args.sync, log)
    if api_key is None:
        return 0

    if args.concurrency < 1:
        print("--concurrency must be at least 1", file=sys.stderr)
        return 1

    chain = resolve_model_chain(args)
    log.info(
        f"running {len(pending)} page(s) with concurrency={args.concurrency}, "
        f"request_interval={args.request_interval:.1f}s"
    )
    log.info(f"model chain (best first): {' > '.join(chain)}")
    pool = ModelPool(models=chain, log=log)
    log.emit("detail", "processing newest lectures first") if log.verbose else None

    client = create_client(api_key, log)
    limiter = RateLimiter(
        concurrency=args.concurrency,
        min_interval_sec=args.request_interval,
    )
    transcribed, failures, not_attempted = await transcribe_pending(
        client,
        pending,
        pool,
        log,
        limiter,
        args.concurrency,
    )

    if failures:
        await log.stop("retries exhausted on a page", not_attempted)

    log.summary(
        transcribed=transcribed,
        skipped=skipped,
        failed=failures,
        pending=not_attempted,
    )
    if failures:
        return 0 if args.sync else 1

    log.info(f"finished transcribing {transcribed} page(s)")
    return 0


def main() -> int:
    args = parse_args()
    load_env(args.repo_root)
    log = Logger(verbose=args.verbose, repo_root=args.repo_root.resolve())
    lectures_dir = (
        args.lectures_dir.resolve()
        if args.lectures_dir
        else args.repo_root / "courses" / "semester-2" / "dynamical-systems" / "materials" / "lectures"
    )
    if not lectures_dir.is_dir():
        print(f"Lectures directory not found: {lectures_dir}", file=sys.stderr)
        return 1

    log.info(f"scanning {lectures_dir}")
    if args.lecture:
        (
            log.emit("detail", f"lecture filter: {args.lecture!r}")
            if args.verbose
            else None
        )
    if args.page:
        log.emit("detail", f"page filter: {args.page!r}") if args.verbose else None
    if args.verbose:
        log.emit("detail", f"models: {', '.join(resolve_model_chain(args))}")

    all_images = find_lecture_page_images(lectures_dir, args.lecture, args.page)
    if not all_images:
        log.info("no page images found")
        return 0

    log.info(f"found {len(all_images)} page image(s)")

    pending: list[Path] = []
    skipped = 0
    for image_path in all_images:
        sidecar = ocr_sidecar_path(image_path)
        should_run, reason = transcription_status(image_path, sidecar, args.force)
        if should_run:
            pending.append(image_path)
            log.pending(image_path, reason)
        else:
            skipped += 1
            log.skip(image_path, reason)

    if not pending:
        log.info(
            f"all {len(all_images)} page(s) already have up-to-date transcriptions"
        )
        log.summary(transcribed=0, skipped=skipped, failed=0, pending=0)
        return 0

    log.info(f"queued {len(pending)} page(s), skipped {skipped}")
    if args.dry_run:
        log.summary(transcribed=0, skipped=skipped, failed=0, pending=len(pending))
        return 0

    return asyncio.run(async_main(args, log, pending, skipped))


if __name__ == "__main__":
    raise SystemExit(main())
