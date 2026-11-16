---
description: "Use the repository's shared Python virtual environment for Python commands, analysis, tests, and tools; do not create or select another environment unless explicitly asked."
applyTo: "**"
---

# Shared Python Environment

- `<repo-root>` is the cursor-study folder that contains `shared/` and `courses/`. In a multi-root workspace, a workspace folder is never the repo root.
- The default interpreter is `<repo-root>/.venv/bin/python`. Resolve it to an absolute path at runtime and pass that path to environment configuration and execution tools. Do not start interactive interpreter selection.
- Use the root `.venv` for Python commands, analysis, tests, PDF extraction, and general scripting, including in course workspaces.
- Do not create a new virtual environment, or use `shared/.venv`, unless the user asks.
- A course-specific `courses/<semester>/<course>/.venv` is only for course code that needs imports the root venv lacks, or when the user asks. See the "Python environments" section of `README.md`.
- The lecture-sync scripts use their own `scripts/.venv-lectures`.
- If the default interpreter is missing or unusable, report it rather than creating or choosing another environment.