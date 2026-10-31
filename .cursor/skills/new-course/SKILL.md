---
name: new-course
description: >-
  Set up a new course in this repo. Use when the user says they want to add
  a new course, start studying a new subject, or set up a new course workspace.
---

# New course setup

Follow these steps in order. Collect missing information from the user before creating files.

## Step 1 — Gather required information

You need the following. Ask for anything not provided:

| Field | Example | Notes |
|-------|---------|-------|
| Course display name | `Linear Algebra` | How it appears in rules and workspace |
| Course ID (slug) | `linear-algebra` | Lowercase, hyphen-separated; derive from name and confirm |
| Semester | `2025-26` | Free text |
| OneNote notebook name | `MSC_CS` | Exact or partial name (match_mode: contains) |
| OneNote section group | `Linear Algebra` | Optional — leave empty if section is directly in notebook |
| OneNote section name | `lectures` | Usually "lectures" |
| Course domain summary | `Linear algebra: vectors, matrices, eigenvalues, transformations` | 1–2 sentences for the AI rule |

**Tip:** if the user is unsure of notebook/section names, tell them to run this after setup:
```bash
./scripts/export_lectures.sh -ShowCatalog
```
This lists all open OneNote notebooks and sections without exporting anything. They can fill in the config and re-run the full export once they know the right names.

## Step 2 — Create the course folder structure

```bash
mkdir -p courses/<id>/materials/{lectures,assignments,syllabus}
mkdir -p courses/<id>/.cursor/rules
```

## Step 3 — Create `courses/<id>/onenote_export_config.json`

One file holds both the course identity and the export config (the PS script ignores unknown fields):

```json
{
  "id": "<id>",
  "name": "<display name>",
  "semester": "<semester>",
  "notebookName": "<notebook name>",
  "sectionGroupName": "<section group or empty string>",
  "sectionName": "<section name>",
  "matchMode": "contains",
  "includeSubpages": false
}
```

## Step 4 — Create the course workspace file

Create `courses/<id>/<id>.code-workspace`:

```json
{
  "folders": [
    { "path": "../../shared", "name": "shared" },
    { "path": ".", "name": "<display name>" }
  ],
  "settings": {
    "terminal.integrated.cwd": "${workspaceFolder:<display name>}",
    "python.defaultInterpreterPath": "${workspaceFolder:<display name>}/../../scripts/.venv-lectures/bin/python",
    "python.analysis.venvPath": "${workspaceFolder:<display name>}/../../scripts",
    "python.analysis.venv": ".venv-lectures"
  }
}
```

## Step 5 — Add course-specific AI guidance

Create `courses/<id>/.cursor/rules/<id>.mdc`:

```markdown
---
description: Context for the <display name> course
globs: materials/**
alwaysApply: false
---

# <display name>

<domain summary>

The lecture-notes skill (`shared/.cursor/skills/lecture-notes/SKILL.md`) has the full workflow for reading handwritten lecture notes.
```

If the course requires unique study workflows (e.g. no handwritten notes), create a course-specific skill in `courses/<id>/.cursor/skills/<id>/SKILL.md` and reference it in the rule.

## Step 6 — Verify

Tell the user:

1. Open `courses/<id>/<id>.code-workspace` in Cursor to start a study session.
2. Run `./scripts/export_lectures.sh -ShowCatalog` (from the repo root) to confirm the OneNote config matches the right notebook/section before doing a real export.
3. When ready to sync lectures, open the workspace and run `../../scripts/export_lectures.sh` from the course folder terminal (or from the repo root: `./scripts/export_lectures.sh`).
