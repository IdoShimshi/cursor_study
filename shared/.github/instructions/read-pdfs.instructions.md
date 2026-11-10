---
description: Read PDFs directly with the file-reading tool first; use code only as fallback
applyTo: "**"
---

# Reading PDFs

For text PDFs in this repo (assignments, syllabus, solutions, exported lecture PDFs), **try the file-reading tool first** (`read_file`, or an attached file):

- A PDF reader may return raw bytes/hex instead of rendered text. Treat that as a failed text read, not as content; do not attempt to interpret PDF internals manually.
- If the read fails, returns empty/garbled text, or omits equations/layout, use PyMuPDF (`pymupdf`) to extract page text. If the VS Code terminal has activated the selected environment, run `python`; otherwise, use `<repo-root>/.venv/bin/python`. Prefer `import pymupdf` (the older `fitz` alias emits a deprecation warning).
- For scanned/image-only PDFs or content not captured by extraction (figures, equation layout, examples), render pages with PyMuPDF to images and inspect the relevant pages. OCR is a fallback for image-only pages, not a reason to install `pdftotext` first.
- Extract all pages needed for the user's request, including neighboring handouts when asked. Keep extracted text as the primary source for readable prose/equations, and visually verify ambiguous equations, symbols, diagrams, and image examples against rendered pages.
- Do not read unrelated course materials unless the user asks; use the specific assignment and its companion handouts first.

If direct reading returns usable text, use it — do not run extraction again just to duplicate the same text. Do not install packages when the shared environment already provides PyMuPDF.

**Handwritten lecture pages:** follow the `lecture-notes` skill (`page-XX.ocr.md`, then `page-XX.png`). That workflow is separate from reading typed PDFs like assignments.
