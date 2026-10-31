---
description: Read PDFs directly with the file-reading tool first; use code only as fallback
applyTo: "**"
---

# Reading PDFs

For text PDFs in this repo (assignments, syllabus, solutions, exported lecture PDFs), **read the file directly** with the file-reading tool (`read_file`, or an attached file):

- Do **not** reach for Python (`pymupdf`/`fitz`), `pdftotext`, or shell extraction unless:
  - Reading the file fails or returns empty/garbled text
  - The PDF is image-only or scanned and needs OCR

If reading works, use its output — do not install packages or run scripts just to re-extract the same text.

**Handwritten lecture pages:** follow the `lecture-notes` skill (`page-XX.ocr.md`, then `page-XX.png`). That workflow is separate from reading typed PDFs like assignments.
