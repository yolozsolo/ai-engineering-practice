---
name: save-progress
description: Inspect repository changes, validate the project, update progress docs, create a sensible commit, and push the branch when safe.
---

# Save Progress

Use this skill when the user asks to save, commit, checkpoint, or push current work.

## Workflow

1. Inspect repository state.
   - Run `git status --short --branch`.
   - Run `git diff --stat`.
   - Run `git diff`.
   - Check for untracked files that may be secrets, large generated files, caches, local data, model artifacts, or vector-store data.

2. Summarize what changed.
   - Group changes by purpose, not by every file.
   - Call out surprising or unrelated changes before staging.
   - Do not stage files that look accidental.

3. Run validation.
   - Run `uv run ruff check .`.
   - Run `uv run mypy .`.
   - Run `uv run pytest`.
   - If a narrower command is more useful, run it too, but do not skip the repository-level checks unless the user explicitly asks.

4. Handle failures.
   - If any validation command fails, explain the failure concisely.
   - Do not commit when checks fail unless the user explicitly asks to commit anyway.
   - If the failure is expected because a starter challenge intentionally contains TODOs, say so and ask before committing.

5. Update documentation.
   - Update `docs/progress.md` with today's date.
   - Include what was built, what was learned, what is still weak, and what to do next.
   - Update `docs/AI.md` when project structure, workflow, active tools, or learning goals changed.

6. Commit.
   - Inspect `git status --short` again before staging.
   - Stage only relevant files.
   - Use a concise commit message, such as `Add raw chunking challenge`.
   - Prefer one coherent commit over mixing unrelated work.

7. Push.
   - Confirm the current branch and upstream with `git status --short --branch`.
   - Push with `git push`.
   - Ask for confirmation before pushing if there are surprising changes, unrelated files, failed checks, or a branch/remote mismatch.

## Safety Rules

- Do not commit secrets, `.env` files, virtual environments, caches, downloaded datasets, local vector stores, model files, or generated outputs.
- Inspect both `git status` and `git diff` before committing.
- Prefer small commits that match one learning milestone.
- Do not rewrite history unless the user explicitly asks.
