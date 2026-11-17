---
name: new-course
description: Set up a new course in this repo. Use when the user says they want to add a new course, start studying a new subject, or set up a new course workspace.
---

# New course setup

The repo root is the directory containing `.git` and `requirements.txt`. Follow these steps in order. Collect missing information from the user before creating files.

## Step 1 — Gather required information

**Look up the course first.** Do not ask the user for a description. Find the course in the Weizmann catalog yourself and take the course name, description, lecturers, and syllabus from it. The user only needs to give the course name (and semester if it is ambiguous). Use the recipe in `/memories/weizmann-course-lookup.md` when available. Summary of the method:

1. Query the catalog with `curl` (the browser cannot reach the site). Use the current academic year (end-year, so fall 2026 is `2027`) and field `40` (Mathematics and Computer Science) unless the course is in another field:
   `https://erez.weizmann.ac.il/apx/f?p=186:20:0::::P20_YEAR,P20_FIELD,P20_SEMESTER,P20_DAY,P20_OBLIG_ELECT,P20_CORE_BASIC,P20_COURSE_TYPE,P20_LECT,P20_COURSE:2027,40,0,0,0,0,0,,<course name, URL-encoded>`
2. Matching is partial and case-insensitive; every word typed must appear in the title. Use a distinctive part of the name if the full title fails.
3. Each result title links to `javascript:det(...,<pid>,...)`. Take that `pid`.
4. Fetch the course page: `https://erez.weizmann.ac.il/apx/r/ws1/186/30?pid=<pid>&pprev=15375`.
5. Strip the HTML to text and keep the course details and syllabus. Save the text word for word as `materials/syllabus/syllabus.md` (see Step 2b).
6. Write the course description for the instructions file (Step 5) from the syllabus text, in 2–4 sentences.

If no result or several results appear, show the matches and ask the user to pick one. Ask only for values the catalog does not give.

You need the following. Use the catalog values where they exist, and ask only for anything not found:

| Field | Example | Notes |
|-------|---------|-------|
| Course display name | `Linear Algebra` | How it appears in instructions and workspace |
| Course ID (slug) | `linear-algebra` | Lowercase, hyphen-separated; derive from name and confirm |
| Semester | `2` | Used in the folder path `courses/semester-<number>/` |
| OneNote notebook name | `MSC_CS` | Exact or partial name (match_mode: contains) |
| OneNote section group | `Linear Algebra` | Optional — leave empty if section is directly in notebook |
| OneNote section name | `lectures` | Usually "lectures" |
| Course domain summary | `Linear algebra: vectors, matrices, eigenvalues, transformations` | 1–2 sentences for the AI instructions |

**Tip:** if the user is unsure of notebook/section names, tell them to run this after setup:
```bash
./scripts/export_lectures.sh -ShowCatalog
```
This lists all open OneNote notebooks and sections without exporting anything. They can fill in the config and re-run the full export once they know the right names.

## Step 2 — Create the course folder structure

```bash
mkdir -p courses/semester-<number>/<id>/materials/{lectures,assignments,syllabus}
mkdir -p courses/semester-<number>/<id>/.github/instructions
```

### Step 2b — Save the course page as the syllabus

Write the course page text from Step 1 to `courses/semester-<number>/<id>/materials/syllabus/syllabus.md`. Keep the content word for word, under a heading with the course title and the source URL. Keep all catalog fields (code, lecturers, schedule, prerequisites, grading, syllabus text).

## Step 3 — Create `courses/semester-<number>/<id>/onenote_export_config.json`

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

Create `courses/semester-<number>/<id>/<id>.code-workspace`. It uses the shared project venv at the repo root (`../../../.venv`); a course can later get its own `.venv` by changing the interpreter path to `${workspaceFolder:<display name>}/.venv/bin/python`.

```json
{
  "folders": [
    { "path": "../../../shared", "name": "shared" },
    { "path": ".", "name": "<display name>" }
  ],
  "settings": {
    "terminal.integrated.cwd": "${workspaceFolder:<display name>}",
    "python.defaultInterpreterPath": "${workspaceFolder:<display name>}/../../../.venv/bin/python",
    "python.analysis.venvPath": "${workspaceFolder:<display name>}/../../..",
    "python.analysis.venv": ".venv"
  }
}
```

## Step 5 — Add course-specific AI guidance

Create `courses/semester-<number>/<id>/.github/instructions/<id>.instructions.md`:

```markdown
---
description: Context for the <display name> course
applyTo: "**/materials/**"
---

# <display name>

<domain summary>

The `lecture-notes` skill (`shared/.github/skills/lecture-notes/SKILL.md`) has the full workflow for reading handwritten lecture notes.
```

If the course requires unique study workflows (e.g. no handwritten notes), create a course-specific skill in `courses/semester-<number>/<id>/.github/skills/<id>/SKILL.md` (the `name` field must equal the folder name) and reference it in the instructions.

## Step 6 — Verify

Tell the user:

1. Open `courses/semester-<number>/<id>/<id>.code-workspace` in VS Code to start a study session.
2. Run `./scripts/export_lectures.sh -ShowCatalog` (from the repo root) to confirm the OneNote config matches the right notebook/section before doing a real export.
3. When ready to sync lectures, open the workspace and run `../../../scripts/export_lectures.sh` from the course folder terminal (or from the repo root: `./scripts/export_lectures.sh`).
