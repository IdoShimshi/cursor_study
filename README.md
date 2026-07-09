# cursor-study

A framework for studying university courses with [Cursor](https://cursor.com). It gives the AI the right context, skills, and tooling to work with lecture notes — without mixing up courses or drowning in irrelevant files.

## The idea

Most course material lives in handwritten notes, PDFs, and assignments scattered across apps. This repo provides:

- **A sync pipeline** — pull handwritten lectures from OneNote, render them as images, and transcribe with OCR
- **Cursor rules & skills** — tell the agent how to read notes, sync with OneNote, and handle math
- **Per-course workspaces** — study one course at a time so the AI only sees what's relevant

Course content stays local and out of git. The repo holds the reusable framework.

## Core concepts

**Framework vs. content.** Scripts, shared rules, and skills live at the repo root. Actual lectures, assignments, and course-specific config live under `courses/<name>/` on your machine.

**One workspace per course.** Open `courses/<name>/<name>.code-workspace` in Cursor when studying. The workspace includes the course folder and `shared/`, but not other courses.

**Skills over prompts.** Instead of repeating instructions every chat, the agent loads skills when needed — e.g. `lecture-notes` for reading, `sync-lectures` for pulling from OneNote, `new-course` for setup.

**Handwritten notes workflow.** Lectures export as PDFs, render to per-page PNGs, and get Gemini OCR sidecars (`page-01.ocr.md`). The agent reads transcriptions first and falls back to images when handwriting is ambiguous.

## Structure

```
cursor-study/
├── scripts/              # OneNote export, PDF rendering, OCR
├── shared/
│   └── .cursor/
│       ├── rules/        # Generic AI rules (math, PDFs, lecture notes)
│       └── skills/       # lecture-notes, sync-lectures
├── courses/              # Your courses (gitignored — local only)
│   └── <course>/
│       ├── materials/    # lectures, assignments, syllabus
│       ├── onenote_export_config.json
│       └── <course>.code-workspace
└── .cursor/skills/       # new-course setup skill
```

## Quick start

1. Clone the repo and copy `.env.example` to `.env` — set `GOOGLE_API_KEY` for OCR.
2. Ask Cursor to **add a new course** (uses the `new-course` skill), or set up `courses/<name>/` manually.
3. Open the course workspace file in Cursor.
4. Run `../../scripts/export_lectures.sh` from the course folder to sync lectures from OneNote.

Requires OneNote desktop on Windows (for export) and WSL if you're on Linux.
