---
name: sync-lectures
description: >-
  Sync lecture notes from OneNote: export PDFs, render pages, and transcribe
  with Gemini OCR. Use when the user asks to sync, update, or pull latest
  lecture notes from OneNote.
---

# Sync lectures

## Repo layout

Scripts are not part of the study workspace. Run them relative to the course folder:

```
<repo>/
  scripts/         ← pipeline (not indexed in study workspace)
  courses/
    <semester>/
      <course>/    ← you are here
        materials/lectures/
        onenote_export_config.json
```

## Run the sync

```bash
../../../scripts/export_lectures.sh
```

This single command runs the full pipeline:

| Step | What it does |
|------|-------------|
| Export | Calls OneNote COM API (Windows), exports changed pages as PDFs to `materials/lectures/` |
| Render | Converts each PDF to `page-01.png`, `page-02.png`, ... |
| Transcribe | Sends new/stale PNGs to Gemini (`gemini-2.5-flash`), writes `page-XX.ocr.md` sidecars |

All steps are **incremental** — safe to run every time:
- Export skips pages whose `lastModifiedTime` hasn't changed
- Render skips PDFs that already have up-to-date PNGs
- Transcribe skips pages with a newer `page-XX.ocr.md` than the PNG

**Success output looks like:** `skipped (unchanged): N` / `skip` per PDF / `skip` per page.

## Requirements

- OneNote desktop (Windows) must be open and synced to the right notebook
- `GOOGLE_API_KEY` set in `.env` at the repo root (two levels up)

If either requirement is missing the script will fail with a clear error. In that case, answer from existing files in `materials/lectures/` and tell the user what's needed.

## Transcription only (manual OCR)

Use these when you only need to re-transcribe, not re-export:

```bash
../../../scripts/gemini_ocr_lectures.sh --dry-run              # list pages missing/stale transcription
../../../scripts/gemini_ocr_lectures.sh                        # transcribe missing/stale only
../../../scripts/gemini_ocr_lectures.sh --lecture "Lecture 3"  # one lecture
../../../scripts/gemini_ocr_lectures.sh --force                # re-transcribe everything
```

## Inspect available OneNote notebooks/sections

```bash
../../../scripts/export_lectures.sh -ShowCatalog
```

Useful when setting up a new course or debugging a mismatch in `onenote_export_config.json`.
