---
description: Compute course math with code instead of hand calculation
applyTo: "**"
---

# Compute with code

When answering **math questions for this course** (lectures, assignments, problem sets, exam prep), prefer **running code** over mental arithmetic or symbolic manipulation in the model.

## Default: compute

Run Python for anything beyond trivial steps. Use **NumPy**, **SciPy**, and **SymPy** as appropriate.

### Execution environment

Use the project virtual environment at the repo root:

- **Path:** `/home/ido/code/msc/cursor_study/.venv`
- **Activation:** `source /home/ido/code/msc/cursor_study/.venv/bin/activate`

If the current course folder has its own `.venv` (e.g. `courses/<course>/.venv`), prefer that one instead.

**Example:**
```bash
source /home/ido/code/msc/cursor_study/.venv/bin/activate && python3 script.py
```

Execute the code and base the answer on the output.

## When reasoning alone is fine

Skip code only when the task is clearly simple, e.g.:

- Small integer arithmetic
- Obvious sign or stability arguments with no numbers
- Conceptual explanations with no precise values requested

If unsure whether a step is "simple enough," run the code.

## Do not

- Guess numeric results, decimals, or long expressions from memory
- Present unverified hand-derived numbers as final answers
