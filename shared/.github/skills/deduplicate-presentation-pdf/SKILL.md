---
name: deduplicate-presentation-pdf
description: Reduce long PDFs exported from slide presentations when consecutive pages are cumulative builds of the same slide. Use when the user asks to deduplicate a PDF, or when a long PDF appears to contain repeated incremental slides and deduplication would help inspect or study it.
---

# Deduplicate presentation PDFs

Use the repository script `scripts/deduplicate_incremental_pdf.py` to collapse consecutive presentation-build pages. This is especially useful when a PDF looks unusually long because each slide's bullets, images, or equations were exported as a separate cumulative page.

## When to use

- Use when the user explicitly asks to deduplicate a PDF.
- Also consider it when working with a long PDF that appears to contain many consecutive incremental/build versions of the same slide. Offer or run it when it would make the PDF easier to inspect or study; do not apply it to ordinary multi-page documents with distinct pages.
- Do not replace or overwrite the source PDF. The script writes a separate output by default.
- After running it, tell the user where the output was written and, when they want to review it, link/open the output PDF.

## How to run when asked

The script is at the repository root under `scripts/`. From the repository root, run it with the project Python interpreter and the input PDF path:

```bash
.venv/bin/python scripts/deduplicate_incremental_pdf.py path/to/input.pdf
```

By default this creates a sibling PDF named `<input-stem>_deduplicated.pdf`. There is no JSON report. The script prints the before/after page counts and grouped ranges to the console.

To choose the output filename, pass it as the second positional argument:

```bash
.venv/bin/python scripts/deduplicate_incremental_pdf.py path/to/input.pdf path/to/output.pdf
```

If the current working directory is not the repository root, use the script's absolute path or change to the root first. Quote paths containing spaces.

## Safety and review

The script merges only adjacent pages when earlier informative PDF objects persist on the later page and the earlier page's rendered foreground is not substantially changed. It ignores whitespace-only glyphs, unstable PDF object numbers, invisible zero-opacity rectangles, white mask fills, and small thin-line changes that can arise as slide builds are revealed. It keeps the last page of each merged group.

This is a conservative heuristic, not a guarantee: rendering thresholds and unusual transparency, animation, masks, or thin details can produce false positives or negatives. Keep the original PDF and visually review the output, especially pages with images, overlaid text, equations, diagrams, or timeline connectors. If a page appears incorrectly merged or left separate, compare that pair in the original and inspect the script's object/visibility logic before changing thresholds broadly.

The script requires PyMuPDF and NumPy; the repository `.venv` already includes them.
