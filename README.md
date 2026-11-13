# cursor-study

A framework for studying university courses with AI assistance in VS Code. It gives the AI the right context, skills, and tooling to work with lecture notes — without mixing up courses or drowning in irrelevant files.

## The idea

Most course material lives in handwritten notes, PDFs, and assignments scattered across apps. This repo provides:

- **A sync pipeline** — pull handwritten lectures from OneNote, render them as images, and transcribe with OCR
- **Instructions & skills** — tell the agent how to read notes, sync with OneNote, and handle math
- **Per-course workspaces** — study one course at a time so the AI only sees what's relevant

Course content stays local and out of git. The repo holds the reusable framework.

## Core concepts

**Framework vs. content.** Scripts, shared rules, and skills live at the repo root. Actual lectures, assignments, and course-specific config live under `courses/<semester>/<name>/` on your machine.

**One workspace per course.** Open `courses/<semester>/<name>/<name>.code-workspace` in VS Code when studying. The workspace includes the course folder and `shared/`, but not other courses.

**Skills over prompts.** Instead of repeating instructions every chat, the agent loads skills when needed — e.g. `lecture-notes` for reading, `sync-lectures` for pulling from OneNote, `new-course` for setup.

**Handwritten notes workflow.** Lectures export as PDFs, render to per-page PNGs, and get Gemini OCR sidecars (`page-01.ocr.md`). The agent reads transcriptions first and falls back to images when handwriting is ambiguous.

## Structure

```
cursor-study/
├── .venv/                # Project venv (numpy/scipy/sympy/matplotlib + OCR deps)
├── requirements.txt      # Deps for the project venv
├── scripts/              # OneNote export, PDF rendering, OCR (own .venv-lectures)
├── shared/
│   └── .github/
│       ├── instructions/ # Generic AI instructions (math, PDFs, lecture notes)
│       └── skills/       # lecture-notes, sync-lectures, new-course
├── courses/              # Your courses (gitignored — local only)
│   └── semester-<number>/
│       └── <course>/
│           ├── materials/    # lectures, assignments, syllabus
│           ├── .github/      # Course-specific instructions/skills
│           ├── onenote_export_config.json
│           └── <course>.code-workspace
└── .github/              # Repo overview (copilot-instructions.md)
```

## Branches

- **`main`** — the framework only: `scripts/`, `shared/`, root config, and this README. `courses/` is empty here.
- **`study`** — `main` plus your actual course content (`courses/<semester>/<name>/`, including course-specific instructions, skills, and workspace files).

`study` always sits on top of `main`. Framework changes are committed on `main` and then merged into `study`; course changes are committed on `study` only.

## Python environments

- **Root `.venv`** — default for the whole project and for all course workspaces. Create with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
- **Per-course venv (optional)** — create `courses/<semester>/<course>/.venv` and point that course's `.code-workspace` interpreter at it.
- **`scripts/.venv-lectures`** — created automatically by the pipeline shell scripts; independent of the above.

## Quick start

1. Clone the repo and copy `.env.example` to `.env` — set `GOOGLE_API_KEY` for OCR.
2. Create the root venv (see above), then ask the agent to **add a new course** (uses the `new-course` skill), or set up `courses/<semester>/<name>/` manually.
3. Open the course workspace file in VS Code.
4. Run `../../../scripts/export_lectures.sh` from the course folder to sync lectures from OneNote.

Requires OneNote desktop on Windows (for export) and WSL if you're on Linux.
