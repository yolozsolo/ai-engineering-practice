# Agent Instructions

This is a local-first AI engineering practice repository.

The goal of this repository is to practice modern AI engineering patterns with free or local-first tools.

Primary topics:

* RAG systems
* MCP servers and clients
* tool-calling loops
* LangGraph workflows
* multi-agent orchestration
* evaluation pipelines
* observability and tracing
* local model usage with Ollama

## Default Behavior

Use `uv` for all Python commands.

For the whole project, prefer:

```
uv run pytest
uv run ruff check .
uv run mypy .
```

For a single challenge file, prefer:

```
uv run python challenges/<file>.py
uv run pytest challenges/<file>.py
uv run ruff check challenges/<file>.py
uv run mypy challenges/<file>.py
```

## Coding Style

Use:

* Python 3.12+
* type hints for public functions
* small functions
* explicit data models with Pydantic, dataclasses, or TypedDict
* deterministic tests
* clear error handling
* simple local-first implementations before adding frameworks

Avoid:

* hidden cloud dependencies
* paid APIs by default
* unnecessary abstractions
* large framework-heavy solutions before the simple version is understood

## Project Modes

The repository has two main modes.

### Challenge Mode

Use `challenges/` for small, self-contained practice tasks.

A challenge should usually fit in one file and include:

* CHALLENGE DESCRIPTION
* GIVEN / STARTER DATA
* IMPLEMENTATION AREA
* EXPECTED BEHAVIOR
* SELF-CHECK / TESTS
* WRITTEN ANSWERS

Starter challenge files should not include the full solution unless explicitly requested.

### Project Mode

Use `src/ai_engineering_practice/` for reusable implementation code.

When a challenge produces useful reusable logic, extract it into `src/`.

## AI Engineering Rules

Every non-trivial AI workflow should have:

* input schema
* output schema
* failure mode handling
* retry or fallback strategy where appropriate
* trace or log record
* at least one evaluation or regression test

Do not treat a working demo as complete unless it is testable and debuggable.

## RAG Rules

RAG tasks should consider:

* document loading
* chunking strategy
* metadata design
* embedding model
* vector store
* retrieval method
* reranking, if relevant
* answer generation
* source attribution
* evaluation

For early practice, prefer implementing the raw mechanics first before hiding everything behind a framework.

Recommended order:

1. raw Python RAG
2. FAISS-based RAG
3. LlamaIndex RAG
4. LangChain or LangGraph-integrated RAG
5. evaluated RAG with Ragas or another eval tool

## Agent Rules

Agent tasks should define:

* state shape
* available tools
* tool schemas
* routing logic
* stopping condition
* maximum iteration count
* error handling
* final response format

Agents must not run unbounded loops.

Agents should expose enough trace information to understand:

* what the model decided
* which tool was called
* what input was passed to the tool
* what the tool returned
* why the loop stopped

## MCP Rules

MCP tasks should separate:

* server implementation
* tool schema
* client integration
* permissions and safety
* malformed input handling
* tests for tool behavior

Prefer small MCP servers first.

Good first MCP tools:

* list_notes
* read_note
* search_notes
* summarize_file
* calculate_value

Avoid giving MCP tools broad filesystem or shell access without explicit safety checks.

## Evaluation Rules

Evaluation tasks should define:

* eval dataset
* expected behavior
* metric or scoring method
* acceptable threshold
* regression test command

For RAG evaluation, consider:

* answer correctness
* faithfulness
* context precision
* context recall
* source attribution
* hallucination risk

For tool or agent evaluation, consider:

* correct tool selection
* valid tool arguments
* successful stopping
* useful final answer
* no unnecessary tool calls

## Observability Rules

For workflows involving LLM calls, retrieval, or tools, prefer structured logs or traces.

A useful trace should include:

* user input
* retrieved context
* selected tool
* tool arguments
* tool result
* model output
* final answer
* error details, if any

Langfuse can be used later for local/self-hosted observability.

## Local-First Tooling Preference

Default local/free stack:

* Ollama for local models
* FAISS for lightweight vector search
* Chroma or Qdrant for vector database practice
* LangGraph for agent orchestration
* LangChain MCP adapters for MCP integration
* LlamaIndex for RAG experiments
* Ragas for RAG evaluation
* pytest for regression tests
* ruff and mypy for code quality

Do not introduce cloud services unless explicitly requested.

## Review Behavior

When reviewing code:

* inspect the relevant files first
* run the relevant command if possible
* explain the main issue clearly
* separate correctness, design, testing, and interview-readiness feedback
* do not rewrite the full solution unless requested

When the user asks for hints, give hints before code.

When the user asks for grading, be strict and practical.

## Documentation Rule

Keep `docs/AI.md` current.

When project structure, workflow, active tools, or learning goals change, update `docs/AI.md` in the same change set.

Also keep `docs/progress.md` updated with:

* what was built
* what was learned
* what is still weak
* what to do next


