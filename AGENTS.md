# AGENTS.md

## Coding conventions

## Python

- Use the latest installed Python version
- use strong typing and type hints
- always add docstrings to functions and classes

## Evals

- All evals are contained in the `evals/` folder
- All skills are contained in the `skills/` folder
- Always create workspace directories in the `evals/` folder adjacent to the skill's eval folder, e.g. for `evals/<skill>/` create `evals/<skill>-workspace/` — never under `skills/`
- Before starting a new iteration, check `evals/<skill>-workspace/` for existing `iteration-N/` folders and number the new one one past the highest found — don't assume `iteration-1` is free
- On Windows, `eval-viewer/generate_review.py` can crash on startup with `UnicodeEncodeError` (the console encoding can't render its box-drawing separator line) — set `PYTHONIOENCODING=utf-8` before running it
- `scripts/aggregate_benchmark.py` requires numeric values in `grading.json`'s `timing.*` and `execution_metrics.*` fields — use `0`/`null` or omit the field for unavailable data, never a placeholder string like `"not available"`, or aggregation crashes