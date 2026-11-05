#!/usr/bin/env python3
"""Collapse consecutive PowerPoint build pages when prior content persists.

A pair is merged only if every informative text glyph, image use, vector
drawing, link, and annotation on the earlier page is also present on the later
page, and the earlier page's visible foreground remains visible when rendered.
The content-object check catches removed hidden objects; the render check catches
objects that remain in the PDF but are painted over. Layout whitespace and
volatile PDF object numbers are not treated as information.
The output keeps the last page of each group (the most-complete build state).
"""

from __future__ import annotations

import argparse
import collections
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pymupdf
from scipy import ndimage


def _number(value: float) -> float:
    """Normalize tiny PDF float differences without masking meaningful moves."""
    return round(float(value), 2)


def _rect_tuple(rect: Any) -> tuple[float, float, float, float]:
    return tuple(_number(value) for value in rect)  # type: ignore[return-value]


def _canonical(value: Any) -> Any:
    """Convert PyMuPDF geometry/style values into stable, hashable values."""
    if isinstance(value, pymupdf.Rect):
        return ("rect", *_rect_tuple(value))
    if isinstance(value, pymupdf.Point):
        return ("point", _number(value.x), _number(value.y))
    if isinstance(value, float):
        return _number(value)
    if isinstance(value, (tuple, list)):
        return tuple(_canonical(item) for item in value)
    if isinstance(value, dict):
        return tuple(sorted((key, _canonical(item)) for key, item in value.items()))
    if value is None or isinstance(value, (str, int, bool, bytes)):
        return value
    return repr(value)


def page_objects(page: pymupdf.Page) -> collections.Counter[tuple[Any, ...]]:
    """Return a multiset of content signatures, including occluded paint ops."""
    signatures: collections.Counter[tuple[Any, ...]] = collections.Counter()

    # get_texttrace reports glyphs and their positions rather than text blocks,
    # allowing a text block to grow incrementally while retaining old glyphs.
    for trace in page.get_texttrace():
        style = (
            trace.get("font"),
            _number(trace.get("size", 0)),
            trace.get("type"),
            trace.get("colorspace"),
            _canonical(trace.get("color")),
            _number(trace.get("opacity", 1)),
            trace.get("layer"),
        )
        for char in trace.get("chars", ()):
            codepoint, glyph_id, origin, bbox = char[:4]
            # PowerPoint exports invisible empty bullet placeholders as runs of
            # literal spaces. Their positions change as bullets are revealed,
            # but they carry no content and must not prevent a merge.
            if chr(codepoint).isspace():
                continue
            signatures[
                (
                    "text",
                    codepoint,
                    glyph_id,
                    style,
                    _canonical(origin),
                    _rect_tuple(bbox),
                )
            ] += 1

    # digest identifies image bytes; bbox + transform distinguish separate
    # placements, including repeated or partly covered images.
    for image in page.get_image_info(xrefs=True):
        signatures[
            (
                "image",
                image.get("digest"),
                image.get("width"),
                image.get("height"),
                image.get("colorspace"),
                image.get("bpc"),
                image.get("has-mask"),
                _rect_tuple(image["bbox"]),
                _canonical(image.get("transform")),
            )
        ] += 1

    # Include complete path geometry and paint style, not just visible bounds.
    for drawing in page.get_drawings():
        # PowerPoint sometimes enlarges a no-paint/clipping rectangle as new
        # text is revealed. Those paths are not visible ink (stroke_opacity=0)
        # and should not count as missing information.
        if drawing.get("fill") is None and drawing.get("stroke_opacity") == 0:
            continue
        # Pure white, un-stroked fills on these white slides act as erasers /
        # masks, not visible slide content. A later build may remove the mask
        # and reveal additional material; that is an addition, not a loss of
        # anything visible on the earlier page. The raster preservation check
        # separately guards all previously visible foreground content.
        fill = drawing.get("fill")
        if (
            fill is not None
            and drawing.get("color") is None
            and all(channel >= 0.99 for channel in fill)
        ):
            continue
        normalized = {
            key: value
            for key, value in drawing.items()
            if key not in {"seqno", "layer"}
        }
        signatures[("drawing", _canonical(normalized))] += 1

    # Preserve actual link targets and rectangles, but ignore xref: it is a
    # document-internal object number that changes when PowerPoint rewrites a
    # page and does not change the link's meaning.
    for link in page.get_links():
        stable_link = {key: value for key, value in link.items() if key != "xref"}
        signatures[("link", _canonical(stable_link))] += 1

    # Annotations carry information independent of rendered page content.
    for annot in page.annots() or ():
        signatures[
            (
                "annotation",
                annot.type,
                _rect_tuple(annot.rect),
                _canonical(annot.info),
                _canonical(annot.vertices),
                _canonical(annot.colors),
                _number(annot.opacity),
            )
        ] += 1

    return signatures


def missing_objects(
    earlier: collections.Counter, later: collections.Counter
) -> list[str]:
    """Describe object types from the earlier page not found in the later one."""
    missing = earlier - later
    kinds = collections.Counter(signature[0] for signature in missing.elements())
    return [f"{kind}: {count}" for kind, count in sorted(kinds.items())]


def visible_content_loss(
    earlier_page: pymupdf.Page, later_page: pymupdf.Page
) -> dict[str, Any]:
    """Measure earlier foreground pixels changed by later-page paint.

    Comparing only object bounds mistakes transparent or white image areas for
    occlusion. Instead render both pages identically, then check whether
    non-background pixels on the earlier page changed substantially. A modest
    channel tolerance ignores antialiasing noise; requiring several changed
    pixels avoids treating isolated renderer differences as lost content.
    """
    render_scale = 1.0
    pixmaps = [
        page.get_pixmap(
            matrix=pymupdf.Matrix(render_scale, render_scale),
            colorspace=pymupdf.csRGB,
            alpha=False,
        )
        for page in (earlier_page, later_page)
    ]
    earlier_pix, later_pix = pixmaps
    if (earlier_pix.width, earlier_pix.height) != (later_pix.width, later_pix.height):
        return {
            "changed_prior_ink_pixels": -1,
            "prior_ink_pixels": -1,
            "fraction_changed": 1.0,
        }

    shape = (earlier_pix.height, earlier_pix.width, earlier_pix.n)
    before = np.frombuffer(earlier_pix.samples, dtype=np.uint8).reshape(shape)
    after = np.frombuffer(later_pix.samples, dtype=np.uint8).reshape(shape)
    prior_ink = np.any(before < 248, axis=2)
    changed = (
        np.max(np.abs(before.astype(np.int16) - after.astype(np.int16)), axis=2) > 32
    )
    changed_prior_ink_mask = prior_ink & changed
    # A new connector or thin line can darken a single row/column of an older
    # diagram without hiding it. Remove isolated one-pixel seams; broad covered
    # regions survive this small morphological opening.
    meaningful_change = ndimage.binary_opening(
        changed_prior_ink_mask, structure=np.ones((2, 2), dtype=bool)
    )
    changed_prior_ink = int(np.count_nonzero(meaningful_change))
    prior_ink_count = int(np.count_nonzero(prior_ink))
    return {
        "changed_prior_ink_pixels": changed_prior_ink,
        "prior_ink_pixels": prior_ink_count,
        "fraction_changed": round(changed_prior_ink / max(prior_ink_count, 1), 8),
    }


def deduplicate(input_path: Path, output_path: Path) -> dict[str, Any]:
    source = pymupdf.open(input_path)
    if source.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")
    if not source.page_count:
        raise ValueError("The input PDF has no pages.")

    signatures = [page_objects(page) for page in source]
    groups: list[dict[str, Any]] = []
    group_start = 0
    decisions: list[dict[str, Any]] = []

    for index in range(source.page_count - 1):
        missing = missing_objects(signatures[index], signatures[index + 1])
        visibility = {
            "changed_prior_ink_pixels": 0,
            "prior_ink_pixels": 0,
            "fraction_changed": 0.0,
        }
        if not missing:
            visibility = visible_content_loss(source[index], source[index + 1])
        # A few dozen changed pixels can be caused by thin new lines crossing
        # old strokes or renderer antialiasing. Ignore that small localized
        # noise, but reject larger changed regions as probable occlusion.
        merge = not missing and visibility["changed_prior_ink_pixels"] < 32
        decisions.append(
            {
                "pages": [index + 1, index + 2],
                "merged": merge,
                "earlier_page_objects_missing_from_later": missing,
                "visibility_check": visibility,
            }
        )
        if not merge:
            groups.append(
                {
                    "first_page": group_start + 1,
                    "last_page": index + 1,
                    "kept_page": index + 1,
                }
            )
            group_start = index + 1

    groups.append(
        {
            "first_page": group_start + 1,
            "last_page": source.page_count,
            "kept_page": source.page_count,
        }
    )

    result = pymupdf.open()
    for group in groups:
        page_number = group["kept_page"] - 1
        result.insert_pdf(
            source, from_page=page_number, to_page=page_number, links=True, annots=True
        )
    if source.metadata is not None:
        result.set_metadata(source.metadata)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path, garbage=4, deflate=True)
    result.close()
    source.close()

    summary = {
        "input": str(input_path),
        "input_pages": len(signatures),
        "output": str(output_path),
        "output_pages": len(groups),
        "removed_pages": len(signatures) - len(groups),
        "groups": groups,
        "adjacent_comparisons": decisions,
        "comparison": "Earlier page's informative objects must persist on the next page, and fewer than 32 foreground pixels from the earlier rendering may change by more than 32 intensity levels per channel. Whitespace glyphs and volatile link xrefs are ignored.",
        "note": "The output retains the last page in each group. The rendered-pixel visibility check distinguishes actual occlusion from harmless geometric overlap, such as new text placed over a transparent image region.",
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input_pdf", type=Path, help="PDF containing incremental slide builds"
    )
    parser.add_argument(
        "output_pdf",
        nargs="?",
        type=Path,
        help="output path (default: <input>_deduplicated.pdf)",
    )
    args = parser.parse_args()

    output = args.output_pdf or args.input_pdf.with_name(
        f"{args.input_pdf.stem}_deduplicated.pdf"
    )
    try:
        summary = deduplicate(args.input_pdf, output)
    except (OSError, ValueError, pymupdf.FileDataError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(
        f"Pages: {summary['input_pages']} -> {summary['output_pages']} "
        f"({summary['removed_pages']} removed)"
    )
    print(f"PDF: {summary['output']}")
    print(
        "Groups: "
        + ", ".join(
            f"{g['first_page']}-{g['last_page']}→{g['kept_page']}"
            for g in summary["groups"]
            if g["first_page"] != g["last_page"]
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
