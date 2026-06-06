---
name: generate-challenge
description: Generate the next small local-first AI engineering practice challenge with starter code, TODOs, tests, and progress tracking.
---

# Generate Challenge

Use this skill when the user asks to create a new practice challenge.

## Inputs

Infer these from the user request when possible:

- Topic: RAG, MCP, tool-calling, LangGraph, multi-agent systems, evaluations, observability, or another AI engineering topic.
- Difficulty: `A`, `B`, or `C`.
- Estimated timebox.
- Whether to create starter-only files or a full solution.

Ask a short clarification question only when the missing input would materially change the challenge. Default to starter-only unless the user explicitly asks for a full solution.

## Default Output

- Create one challenge file under `challenges/`.
- Create one matching pytest file under `tests/`.
- Do not fully solve the challenge unless explicitly requested.
- Include TODO sections in the implementation area.
- Include starter data when useful.
- Include clear expected behavior.
- Include deterministic tests where possible.
- Keep the task local-first and free-tool compatible.
- Update `docs/progress.md` with the generated task as the next active task.
- Update `docs/AI.md` only if workflow, structure, tools, or learning goals changed.

## Challenge Format

Each challenge file should usually include:

- `CHALLENGE DESCRIPTION`
- `GIVEN / STARTER DATA`
- `IMPLEMENTATION AREA`
- `EXPECTED BEHAVIOR`
- `SELF-CHECK / TESTS`
- `WRITTEN ANSWERS`

Use plain Python first. Add frameworks only when the challenge topic is specifically about that framework.

## Naming

- Use sequential challenge numbers.
- Challenge files should look like `001_raw_chunking.py`.
- Test files should look like `test_001_raw_chunking.py`.
- Determine the next number by inspecting existing files in `challenges/` and `tests/`.

## Recommended Early Sequence

1. Raw chunking.
2. Ollama embeddings wrapper.
3. FAISS similarity search.
4. Raw RAG with answer and sources.
5. Simple RAG eval dataset.
6. Manual tool-calling loop.
7. LangGraph state machine.
8. MCP notes server.
9. Agent loop with stopping conditions.
10. Multi-agent researcher/reviewer.

## Validation

Run the most relevant checks for the files created:

- `uv run pytest tests/<test_file>.py`
- `uv run ruff check challenges/<challenge_file>.py tests/<test_file>.py`

It is acceptable for starter challenge tests to fail because TODOs are intentionally incomplete. Confirm that failures are due to the TODOs, not import errors or broken test setup.
