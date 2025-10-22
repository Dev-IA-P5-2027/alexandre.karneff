## Purpose

This repository is a small collection of Python Jupyter notebooks with beginner/intermediate exercises (French). This document gives concise, actionable guidance for an AI coding agent to be immediately productive when editing, running, or refactoring the notebooks.

## Quick facts
- Layout: top-level folders `01/`, `01bis/`, `02/` each contain a notebook named like `01_Exercices_grand_debutant.ipynb`.
- Primary language: Python (notebook code cells). Comments and exercise text are typically in French.
- No CI, test harness, or requirements file present in the repository root.

## Big-picture architecture
- This is not a multi-module application — it's a set of standalone notebooks for exercises. There are no services, databases, or packaging conventions to follow.
- Typical flow: open a notebook in `VS Code` or Jupyter, run cells sequentially, edit code in-place. If code needs to be reused across notebooks, extract helper functions into a new Python module under a new folder (for example, `lib/`) and import that module from notebooks.

## Files & conventions to reference
- `02/02_Exercices_intermediaire.ipynb` — an example intermediate exercise notebook. It contains cells like:
  - a loop computing `sin(i)/i` with a `try/except ZeroDivisionError` to avoid division by zero
  - simple list operations (`append`, `index`, `remove`, slicing)
- Notebooks include cell metadata with `language` and `id`. When adding cells, set `metadata.language` to `python` or `markdown`.

## How to run and validate changes (Windows PowerShell examples)
- Interactive (recommended): open the notebook in VS Code and run cells with the Python/Jupyter extension.
- Headless execution (to run all cells and produce an executed notebook):

```powershell
# run and overwrite an executed copy
jupyter nbconvert --to notebook --execute "02/02_Exercices_intermediaire.ipynb" --output "02/02_Exercices_intermediaire.executed.ipynb"
```

- If you need parameterization or repeatable runs, consider installing `papermill`:

```powershell
python -m pip install papermill
papermill "02/02_Exercices_intermediaire.ipynb" "out.ipynb"
```

## Environment and dependencies
- The notebooks use the Python standard library (e.g., `math.sin`) and basic built-ins. Assume Python 3.8+ unless the user specifies otherwise.
- There is no `requirements.txt`. When running CI or local checks, create a virtual environment and install `jupyter` (and `papermill` if needed):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install --upgrade pip jupyter
```

## Editing and content conventions for AI agents
- Preserve existing `metadata.id` values when modifying existing cells. When adding new cells, include `metadata.language`.
- Keep outputs deterministic: avoid non-deterministic RNG or time-based behavior in solutions unless the exercise expects it.
- Small refactors: prefer extracting reusable helpers into modules (e.g., `lib/utils.py`) instead of duplicating logic across notebooks.

## Patterns and examples to follow (concrete)
- Error handling: cells use `try/except` for obvious runtime exceptions. Example pattern from `02/02_Exercices_intermediaire.ipynb`:

```python
from math import sin
for i in range(-3, 4):
    try:
        print(sin(i)/i)
    except ZeroDivisionError:
        print("Erreur : Pas de division par zéro")
```

- List operations are written in-place (mutating): use `append`, `remove`, `index`, and slicing when demonstrating list concepts.

## What NOT to change
- Do not remove or rename the notebooks — they are the canonical exercises for the user.
- Avoid wholesale reformatting of notebook JSON outside minimal edits (adding or editing cells). Keep existing cell ordering unless intentionally reworking an exercise.

## Gaps and suggested follow-ups
- Add a `requirements.txt` or `environment.yml` for reproducible runs.
- Add a small `scripts/run_all_notebooks.ps1` to standardize headless execution.

## If you need more context
- Ask the repo owner for the preferred Python version and any hidden dependencies. Also ask whether they want extracted helper modules committed back into the repo or kept local.

---
If this looks good I can: create a `requirements.txt`, add a sample `lib/` helper module and update `02/02_Exercices_intermediaire.ipynb` to import it. Tell me which follow-up you'd like.
