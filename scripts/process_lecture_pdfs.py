#!/usr/bin/env python3
"""Render lecture PDFs to PNG pages."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RENDER_ZOOM = 2.0
MANIFEST_NAME = "manifest.json"
STALE_TRANSCRIPTION_NOTICE = (
    "**STALE** — page image was re-rendered; transcription pending."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render lecture PDFs to page images."
    )
    parser.add_argument(
        "--lectures-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "courses" / "semester-2" / "dynamical-systems" / "materials" / "lectures",
        help="Directory containing exported lecture PDFs",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render even when PDF has not changed",
    )
    parser.add_argument(
        "--lecture",
        type=str,
        default="",
        help="Process only PDFs whose filename contains this substring",
    )
    return parser.parse_args()


def lecture_asset_dir(pdf_path: Path) -> Path:
    return pdf_path.with_suffix("")


def pdf_mtime(pdf_path: Path) -> float:
    return pdf_path.stat().st_mtime


def load_manifest(asset_dir: Path) -> dict | None:
    manifest_path = asset_dir / MANIFEST_NAME
    if not manifest_path.exists():
        return None
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def needs_render(pdf_path: Path, asset_dir: Path, force: bool) -> bool:
    if force:
        return True
    manifest = load_manifest(asset_dir)
    if manifest is None:
        return True
    if manifest.get("pdf_mtime") != pdf_mtime(pdf_path):
        return True
    expected_pages = manifest.get("page_count", 0)
    for index in range(1, expected_pages + 1):
        if not (asset_dir / f"page-{index:02d}.png").exists():
            return True
    if expected_pages == 0:
        return True
    return False


def mark_sidecars_stale(asset_dir: Path) -> None:
    for sidecar in asset_dir.glob("page-*.ocr.md"):
        content = sidecar.read_text(encoding="utf-8")
        if STALE_TRANSCRIPTION_NOTICE in content:
            continue

        lines = content.splitlines()
        insert_at = 0
        for index, line in enumerate(lines):
            if line.startswith("# "):
                insert_at = index + 1
                break

        while insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1

        lines.insert(insert_at, f"> {STALE_TRANSCRIPTION_NOTICE}")
        if insert_at + 1 == len(lines) or lines[insert_at + 1].strip() != "":
            lines.insert(insert_at + 1, "")

        sidecar.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_pdf(pdf_path: Path, asset_dir: Path) -> list[Path]:
    import fitz

    asset_dir.mkdir(parents=True, exist_ok=True)
    if asset_dir.exists():
        mark_sidecars_stale(asset_dir)
    for stale_png in asset_dir.glob("page-*.png"):
        stale_png.unlink()

    doc = fitz.open(pdf_path)
    rendered: list[Path] = []
    matrix = fitz.Matrix(RENDER_ZOOM, RENDER_ZOOM)
    for index, page in enumerate(doc, start=1):
        output_path = asset_dir / f"page-{index:02d}.png"
        page.get_pixmap(matrix=matrix).save(output_path)
        rendered.append(output_path)
    return rendered


def write_manifest(pdf_path: Path, asset_dir: Path, page_paths: list[Path]) -> None:
    payload = {
        "source_pdf": pdf_path.name,
        "pdf_mtime": pdf_mtime(pdf_path),
        "processed_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(page_paths),
        "pages": [path.name for path in page_paths],
    }
    (asset_dir / MANIFEST_NAME).write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )


def process_pdf(pdf_path: Path, force: bool) -> str:
    asset_dir = lecture_asset_dir(pdf_path)
    if not needs_render(pdf_path, asset_dir, force):
        return f"skip  {pdf_path.name}"

    page_paths = render_pdf(pdf_path, asset_dir)
    write_manifest(pdf_path, asset_dir, page_paths)
    return f"render  {pdf_path.name} ({len(page_paths)} pages)"


def list_pdf_files(lectures_dir: Path, lecture_filter: str) -> list[Path]:
    pdfs = sorted(lectures_dir.glob("*.pdf"))
    if lecture_filter:
        pdfs = [pdf for pdf in pdfs if lecture_filter.lower() in pdf.name.lower()]
    return pdfs


def main() -> int:
    args = parse_args()
    lectures_dir = args.lectures_dir.resolve()
    if not lectures_dir.is_dir():
        print(f"Lectures directory not found: {lectures_dir}", file=sys.stderr)
        return 1

    pdfs = list_pdf_files(lectures_dir, args.lecture)
    if not pdfs:
        print(f"No PDFs found in {lectures_dir}")
        return 0

    results = [process_pdf(pdf_path, force=args.force) for pdf_path in pdfs]
    for line in results:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
