# cursor-study

Framework for studying university courses with AI assistance.

- `scripts/` — OneNote export, PDF rendering, Gemini OCR pipeline (has its own `scripts/.venv-lectures`).
- `shared/.github/` — shared instructions (`instructions/`) and skills (`skills/`: `lecture-notes`, `sync-lectures`, `new-course`).
- `courses/semester-<number>/<course>/` — per-course materials, config, and course-specific instructions/skills in `courses/semester-<number>/<course>/.github/`.

Python: if the VS Code terminal has activated the selected environment, use `python`; otherwise use `<repo-root>/.venv/bin/python`. The default environment is the repository's `.venv` (dependencies in `requirements.txt`).
