# AI Project Context

This repository is a local-first AI engineering practice workspace.

The goal is to practice production-relevant AI engineering patterns:

- RAG pipelines
- MCP servers and clients
- tool-calling loops
- LangGraph workflows
- multi-agent orchestration
- evaluation pipelines
- prompt/version regression tests
- observability and tracing
- local model usage with Ollama

## Preferred Workflow

1. Generate a small challenge or feature.
2. Implement it locally.
3. Run tests and evals.
4. Review the design.
5. Record what was learned in `docs/progress.md`.

## Stack

- Python 3.12+
- uv
- pytest
- ruff
- mypy
- Ollama for local models
- LangGraph for agent orchestration
- LangChain MCP adapters for MCP integration
- LlamaIndex for RAG experiments
- FAISS / Chroma / Qdrant for vector search
- Ragas / DeepEval / promptfoo for evaluation
- Langfuse for observability

## Project Modes

`challenges/` contains small practice tasks.

`src/ai_engineering_practice/` contains reusable implementation code.

Prefer solving in `challenges/` first, then extracting reusable code into `src/`.

## Challenge File Sections

Each challenge should include:

- CHALLENGE DESCRIPTION
- GIVEN / STARTER DATA
- IMPLEMENTATION AREA
- EXPECTED BEHAVIOR
- SELF-CHECK / TESTS
- WRITTEN ANSWERS

Generated starter files should not include the full solution unless explicitly requested.

## Agent Behavior

When helping, act as a senior AI engineering tutor.

- Explain design tradeoffs.
- Keep changes small.
- Prefer local/free tools.
- Avoid cloud dependencies unless explicitly requested.
- Do not hide complexity.
- Ask for evaluation strategy, not only working output.
- Do not grade unless explicitly asked.
- When grading, run tests/evals and give strict practical feedback.

## Maintenance Rule

When workflow, tools, project structure, or active learning goals change, update this file in the same change set.