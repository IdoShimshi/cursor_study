---
description: Compute course math with code instead of hand calculation
applyTo: "**"
---

# Compute with code

When answering **math questions for this course** (lectures, assignments, problem sets, exam prep), prefer **running code** over mental arithmetic or symbolic manipulation in the model.

## Default: compute

Run Python for anything beyond trivial steps. Use **NumPy**, **SciPy**, and **SymPy** as appropriate.

### Execution environment

If the VS Code terminal has activated the selected environment, use `python`. Otherwise, use `<repo-root>/.venv/bin/python` (or the course's `.venv` if it has one). Avoid bare `python3`, which may select the system interpreter.

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
