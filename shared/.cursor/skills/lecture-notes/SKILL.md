---
name: lecture-notes
description: >-
  Read handwritten lecture notes for the active course. Use when answering
  questions about lecture content, finding topics, or studying course material.
---

# Lecture notes

Handwritten OneNote lectures live in `materials/lectures/`. Each lecture PDF has a sibling folder:

```
materials/lectures/2026-05-14_Lecture 3 - 06_05.pdf
materials/lectures/2026-05-14_Lecture 3 - 06_05/
  page-01.png          ← authoritative image
  page-01.ocr.md       ← Gemini transcription sidecar
  manifest.json
```

Before answering a lecture question, use the **sync-lectures** skill to pull the latest from OneNote.

## Typed PDFs vs handwritten pages

- **Assignments, syllabus, solution PDFs:** read the `.pdf` directly with the Read tool (see the `read-pdfs` rule). Do not use Python or `pdftotext` unless Read fails.
- **Handwritten lecture content:** use the OCR/PNG workflow below, not the parent lecture PDF.

## How to answer questions about lecture content

1. **Start with transcriptions** — read `page-XX.ocr.md` in the relevant lecture folder to find topics, notation, and wording.
2. **Quote and cite** — paraphrase from the sidecar when answering; point to the lecture and page (e.g. Lecture 3, page 2).
3. **Fall back to images when needed** — if a transcription is missing, garbled, or ambiguous, open the matching `page-XX.png`. PNGs are authoritative for handwriting and math.
4. **Do not guess** past what transcriptions and images support.

## File roles

| File | Role |
|------|------|
| `page-XX.ocr.md` | Fast text pass; approximate, good for search and relevance |
| `page-XX.png` | Source of truth for handwriting and diagrams |
| `manifest.json` | Render metadata; not lecture content |
