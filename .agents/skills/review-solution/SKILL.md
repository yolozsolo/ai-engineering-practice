---
name: review-solution
description: Review a completed challenge solution for correctness, simplicity, tests, AI engineering relevance, and readiness for commit or extraction.
---

# Review Solution

Use this skill when the user asks for review, grading, feedback, or readiness checks on a completed challenge.

## Workflow

1. Identify the relevant challenge and test files.
   - Inspect the challenge file.
   - Inspect the matching test file.
   - Inspect nearby reusable code if the solution imports from `src/ai_engineering_practice/`.

2. Run relevant checks when possible.
   - Prefer `uv run pytest tests/<test_file>.py`.
   - Run `uv run ruff check <challenge_file> tests/<test_file>.py`.
   - Run `uv run mypy <challenge_file>` when the file structure supports it.
   - If repository-level checks are relevant, run `uv run pytest`, `uv run ruff check .`, or `uv run mypy .`.

3. Review the solution.
   - Check correctness against the challenge requirements.
   - Check simplicity and whether the solution stays focused.
   - Check type hints and data shape clarity.
   - Check edge cases and failure behavior.
   - Check test quality and whether tests prove the intended behavior.
   - Check whether the solution teaches the intended AI engineering concept.

## Feedback Format

Lead with findings when there are bugs or risks. Separate feedback into:

- Correctness.
- Design.
- Tests.
- AI engineering relevance.
- Suggested next step.

Be strict and practical. Do not rewrite the whole solution unless the user explicitly asks.

## Fix Guidance

- Prefer minimal targeted fixes.
- Give hints before code when the user asks for hints.
- Recommend extraction into `src/ai_engineering_practice/` only when the same pattern is likely to be reused across multiple challenges or project features.
- Do not extract code just because the current solution works.
