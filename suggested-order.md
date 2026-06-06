The first learning track I recommend

Do this order.

Track 1: RAG fundamentals
001_raw_chunking.py
002_ollama_embeddings.py
003_faiss_search.py
004_raw_rag_answer_with_sources.py
005_rag_eval_dataset.py

Goal: understand the full RAG path before frameworks.

Track 2: Tool calling and agent loops
006_tool_schema_and_dispatch.py
007_manual_agent_loop.py
008_langgraph_agent_loop.py
009_agent_loop_stopping_conditions.py

Goal: understand that an agent is a loop with state, tools, routing, and stopping.

Track 3: MCP
010_mcp_notes_server.py
011_mcp_client_calling_notes.py
012_langgraph_agent_with_mcp_tools.py

Goal: understand MCP as a tool/context boundary.

Track 4: Evaluation
013_rag_regression_eval.py
014_tool_call_eval.py
015_agent_trace_eval.py

Goal: stop judging AI apps only by “it looked good once.”

Track 5: Mini product
local_rag_api/

Build:

FastAPI /ask endpoint
local RAG
source citations
basic eval set
logs/traces