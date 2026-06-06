Yes. I would create a **separate repo/project**, not just a skill.

A skill is useful later for things like “generate AI challenge”, “review agent solution”, “save progress”, or “create RAG benchmark”, but first you need a clean project shape similar to your current `data-engineering-practice` / interview-practice workflow. Your current project already has a good pattern: lightweight repo, `uv`, single-file challenges, reusable prompts, `AGENTS.md`, and a `docs/AI.md` handoff file that keeps context current. 

## Proposed repo name

```text
ai-engineering-practice
```

Better than `langchain-practice`, because the goal is broader than LangChain:

```text
RAG
MCP
tool calling
agent loops
multi-agent systems
evaluation
observability
local models
structured outputs
prompt/version testing
```

## Main principle

Use **free/local-first tools**, but keep the architecture close to industry practice.

So the stack should be:

```text
Python 3.12+
uv
pytest
ruff
mypy
Ollama
LangGraph
LangChain MCP adapters
LlamaIndex
FastAPI
Chroma or Qdrant local
FAISS for lightweight vector search
Ragas
DeepEval or promptfoo
Langfuse self-hosted
Docker Compose
```

LangGraph is a good default for serious agent orchestration because it focuses on durable execution, streaming, human-in-the-loop, and explicit stateful workflows, rather than only simple “agent magically decides” abstractions. ([LangChain Docs][1]) MCP is worth including because it is becoming the standard interface for giving LLM apps access to tools and context, and LangChain/LangGraph can consume MCP tools through adapters. ([LangChain Docs][2])

For local/free models, use **Ollama**. For embeddings, start with `nomic-embed-text` or `qwen3-embedding`; Ollama’s library currently lists Qwen3 embedding models in several sizes and `nomic-embed-text` as a popular local embedding model. ([Ollama][3])

For observability, use **Langfuse self-hosted**. It is open source, self-hostable, and supports traces, debugging, evaluations, datasets, prompt management, and LLM-app monitoring. ([GitHub][4])

For evaluation, use **Ragas + DeepEval/promptfoo**. Ragas is specifically useful for moving from “vibe checks” to systematic evaluation loops, especially for RAG and agentic workflows. ([docs.ragas.io][5])

---

# Suggested project structure

```text
ai-engineering-practice/
├── README.md
├── AGENTS.md
├── pyproject.toml
├── uv.lock
├── .env.example
├── docker-compose.yml
│
├── docs/
│   ├── AI.md
│   ├── progress.md
│   ├── architecture-notes.md
│   ├── tool-decisions.md
│   └── glossary.md
│
├── prompts/
│   ├── generate-task.md
│   ├── review-solution.md
│   ├── rag-debugging.md
│   ├── agent-design-review.md
│   └── eval-design-review.md
│
├── challenges/
│   ├── 001_basic_rag_pipeline.py
│   ├── 002_tool_calling_loop.py
│   ├── 003_mcp_filesystem_server.py
│   ├── 004_langgraph_react_agent.py
│   ├── 005_rag_eval_ragas.py
│   └── 006_multi_agent_researcher_reviewer.py
│
├── src/
│   └── ai_engineering_practice/
│       ├── __init__.py
│       ├── llms/
│       │   ├── ollama_client.py
│       │   └── model_registry.py
│       ├── rag/
│       │   ├── loaders.py
│       │   ├── chunking.py
│       │   ├── embeddings.py
│       │   ├── vectorstores.py
│       │   ├── retrievers.py
│       │   └── chains.py
│       ├── agents/
│       │   ├── state.py
│       │   ├── tool_loop.py
│       │   ├── langgraph_flows.py
│       │   └── multi_agent.py
│       ├── mcp/
│       │   ├── servers/
│       │   └── clients/
│       ├── evals/
│       │   ├── datasets.py
│       │   ├── ragas_eval.py
│       │   ├── deepeval_eval.py
│       │   └── regression.py
│       ├── observability/
│       │   └── langfuse_tracing.py
│       └── utils/
│           ├── config.py
│           └── logging.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_retrievers.py
│   ├── test_tool_loop.py
│   └── test_evals.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── eval_sets/
│
└── notebooks/
    └── experiments.ipynb
```

This gives you two modes:

```text
challenges/ = interview/practice tasks, small and self-contained
src/        = reusable project code, closer to production structure
```

That is important. For learning, single files are good. For real AI engineering, reusable modules are needed.

---

# Initial dependency setup

Use `uv`.

```bash
mkdir ai-engineering-practice
cd ai-engineering-practice

uv init --package --python 3.12
uv add fastapi uvicorn pydantic pydantic-settings python-dotenv
uv add langchain langgraph langchain-community langchain-ollama langchain-mcp-adapters
uv add llama-index llama-index-llms-ollama llama-index-embeddings-ollama
uv add chromadb faiss-cpu qdrant-client
uv add ragas deepeval langfuse datasets pandas numpy
uv add rich typer httpx tenacity structlog
uv add --dev pytest pytest-cov ruff mypy ipykernel
```

Possible simplification: do **not** use both LlamaIndex and LangChain heavily at first. Keep both installed, but choose this rule:

```text
LangGraph/LangChain = agents, tool loops, MCP, orchestration
LlamaIndex          = RAG experiments, indexing, retrieval abstractions
Raw Python          = exercises where you need to understand the mechanics
```

---

# Local services

Use Docker Compose only for infra-like tools:

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

  langfuse:
    image: langfuse/langfuse:latest
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://langfuse:langfuse@postgres:5432/langfuse
      NEXTAUTH_SECRET: local-dev-secret
      SALT: local-dev-salt
      NEXTAUTH_URL: http://localhost:3000
    depends_on:
      - postgres

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: langfuse
      POSTGRES_PASSWORD: langfuse
      POSTGRES_DB: langfuse
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  qdrant_data:
  postgres_data:
```

For a first version, I would actually start with:

```text
Ollama locally
FAISS in process
Chroma optional
Qdrant later
Langfuse later
```

Do not start with every moving part on day one.

---

# Recommended local models

Start with this:

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
ollama pull nomic-embed-text
ollama pull qwen3-embedding:0.6b
```

Use them like this:

```text
qwen3:8b              general reasoning / agents
llama3.1:8b           comparison baseline
nomic-embed-text      simple RAG embedding baseline
qwen3-embedding:0.6b  stronger embedding experiment
```

Do not over-optimize models at the beginning. Your learning goal is architecture, evaluation, and debugging. Model choice matters, but bad RAG/agent design will fail even with a good model.

---

# `docs/AI.md` for the new project

Create this early.

```md
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
```

This mirrors the best part of your existing setup, where the assistant can regain project context from a compact `docs/AI.md`. 

---

# `AGENTS.md` suggestion

````md
# Agent Instructions

This is a local-first AI engineering practice repository.

## Default behavior

Use `uv` for all commands.

Prefer:

```bash
uv run pytest
uv run ruff check .
uv run mypy .
````

For single challenge files:

```bash
uv run python challenges/<file>.py
uv run pytest challenges/<file>.py
uv run ruff check challenges/<file>.py
uv run mypy challenges/<file>.py
```

## Coding style

* Python 3.12+
* Type hints required for public functions
* Small functions
* Explicit data models with Pydantic or dataclasses
* No hidden cloud dependencies
* No paid APIs by default
* Prefer deterministic tests over manual inspection

## AI engineering rules

Every non-trivial AI workflow should have:

* input schema
* output schema
* failure mode handling
* retry or fallback strategy where appropriate
* trace/log record
* at least one evaluation or regression test

## RAG rules

RAG tasks should consider:

* document loading
* chunking
* metadata
* embeddings
* retrieval
* reranking if relevant
* answer generation
* source attribution
* evaluation

## Agent rules

Agent tasks should consider:

* state shape
* tools available
* stopping condition
* max iterations
* error handling
* human approval for risky actions
* traceability of tool calls

## MCP rules

MCP tasks should separate:

* server implementation
* tool schema
* client integration
* safety/permissions
* tests for malformed tool calls

````

---

# First 10 practice tasks

I would start with these in order.

## 1. Raw RAG pipeline, no framework

Goal: understand the mechanics.

```text
Input: small markdown docs
Steps: chunk -> embed -> FAISS search -> answer with local Ollama model
Output: answer + top source chunks
````

Important learning:

```text
chunk size
overlap
metadata
retrieval score
source grounding
```

## 2. RAG with LlamaIndex

Same dataset, but use LlamaIndex.

Compare:

```text
raw implementation vs framework implementation
```

## 3. LangChain tool-calling loop

Build a simple loop:

```text
question -> model -> tool call -> tool result -> final answer
```

Tools:

```text
calculator
file search
simple JSON lookup
```

Key concept:

```text
agent loop != one LLM call
```

## 4. LangGraph ReAct-style agent

Build the same tool loop in LangGraph.

Practice:

```text
State
nodes
edges
conditional routing
max iterations
final response
```

## 5. MCP filesystem server

Create a tiny MCP server exposing safe tools:

```text
list_notes()
read_note(name)
search_notes(query)
```

Then connect it to a LangGraph agent through MCP adapters.

## 6. RAG evaluation with Ragas

Create a tiny eval dataset:

```text
question
expected_answer
expected_source
```

Measure:

```text
faithfulness
answer relevancy
context precision/recall
```

## 7. Regression test for prompts

Create a test where a prompt change can break behavior.

Example:

```text
Given a support ticket, classify severity and return JSON.
```

Test:

```text
valid JSON
correct enum
no extra prose
stable classification
```

## 8. Multi-agent researcher/reviewer

Agents:

```text
researcher
critic
final_writer
```

Use a bounded loop:

```text
researcher -> critic -> revise -> final
```

Important: max loop count and clear stopping condition.

## 9. Langfuse tracing

Add traces for:

```text
RAG query
retrieval step
LLM generation
tool call
eval score
```

Goal: learn what production debugging looks like.

## 10. Mini AI product

Build a small local app:

```text
FastAPI endpoint
POST /ask
local RAG
tracing
eval test
Docker Compose optional
```

This becomes your portfolio-quality base.

---

# What I would not do first

Avoid this at the beginning:

```text
CrewAI
AutoGen
too many vector DBs
Kubernetes
cloud deployment
fine-tuning
complex UI
paid APIs
```

CrewAI and AutoGen are worth knowing, especially for multi-agent comparisons, but I would not make them the base. Start with LangGraph because it forces you to understand state, control flow, and stopping conditions. AutoGen/CrewAI can become comparison modules later.

---

# Suggested README opening

```md
# AI Engineering Practice

Local-first practice repository for modern AI engineering tasks.

The goal is to build practical skill in:

- RAG systems
- MCP tools
- local LLM usage
- agent loops
- LangGraph orchestration
- multi-agent workflows
- evaluation pipelines
- observability
- production-style AI app structure

This is not a toy prompt collection. Each task should produce runnable code, tests, and a short written design note.
```

---

# My recommended starting setup

Create the repo like this:

```bash
mkdir ai-engineering-practice
cd ai-engineering-practice
uv init --package --python 3.12

mkdir -p docs prompts challenges tests data/raw data/processed data/eval_sets notebooks
mkdir -p src/ai_engineering_practice/{llms,rag,agents,mcp,evals,observability,utils}

touch README.md AGENTS.md docs/AI.md docs/progress.md docs/tool-decisions.md .env.example
```

Then install a smaller starter dependency set first:

```bash
uv add pydantic pydantic-settings python-dotenv rich typer httpx tenacity
uv add langchain langgraph langchain-community langchain-ollama langchain-mcp-adapters
uv add llama-index llama-index-llms-ollama llama-index-embeddings-ollama
uv add faiss-cpu chromadb ragas datasets
uv add --dev pytest pytest-cov ruff mypy ipykernel
```

Later add:

```bash
uv add qdrant-client langfuse deepeval
```

This prevents the first week from becoming dependency hell.

---

# The actual “skill” I would add later

After the repo exists, add a project-specific skill called:

```text
generate-ai-practice-task
```

Purpose:

```text
Generate one runnable AI engineering challenge based on the current learning track.
```

Inputs:

```text
topic: rag | mcp | agent-loop | langgraph | multi-agent | eval | observability
difficulty: A | B | C
mode: challenge | mini-project | review
```

Output:

```text
one challenge file
one test file if needed
updates docs/progress.md
updates docs/AI.md if project context changed
```

But this is second step. First create the project skeleton.

---

My strongest recommendation:

```text
Base project: ai-engineering-practice
Core framework: LangGraph
Local models: Ollama
RAG framework: LlamaIndex + raw implementations
MCP: langchain-mcp-adapters
Vector search: FAISS first, Qdrant later
Evaluation: Ragas first, DeepEval/promptfoo later
Observability: Langfuse self-hosted later
```

This gives you something close to industry practice, while staying free/local and still understandable.
