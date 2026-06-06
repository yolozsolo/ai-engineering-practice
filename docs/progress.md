# Progress

## 2026-06-06

### Built
- Added Challenge 001: raw RAG document chunking.
- Added pytest tests for chunk size splitting, overlap, metadata, document order, and edge cases.
- Added repository-level Codex skills for saving progress, generating challenges, and reviewing solutions.

### Learned
- Chunking is the first retrieval design decision in a RAG pipeline.
- Metadata such as `document_id` and `chunk_index` makes retrieved chunks traceable.
- Repository skills can turn repeated project workflows into explicit reusable instructions.

### Still Weak
- The chunking implementation is intentionally unfinished.
- The current challenge uses character windows only; sentence-aware chunking comes later.
- The repository skills are instruction-only and do not yet automate validation or commit steps.

### Next
- Implement `chunk_text`.
- Implement `chunk_documents`.
- Run `uv run pytest tests/test_001_raw_chunking.py`.
- Try `/skills generate-challenge` or `/skills review-solution` during the next practice loop.
