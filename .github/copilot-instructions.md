# cursor-study

Framework for studying university courses with AI assistance.

- `scripts/` — OneNote export, PDF rendering, Gemini OCR pipeline (has its own `scripts/.venv-lectures`).
- `shared/.github/` — shared instructions (`instructions/`) and skills (`skills/`: `lecture-notes`, `sync-lectures`, `new-course`).
- `courses/<course>/` — per-course materials, config, and course-specific instructions/skills in `courses/<course>/.github/`.

Python: use the project venv at `/home/ido/code/msc/cursor_study/.venv` (dependencies in `requirements.txt`).
