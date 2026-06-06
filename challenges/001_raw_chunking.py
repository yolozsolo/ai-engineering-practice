"""Challenge 001: Raw RAG document chunking.

CHALLENGE DESCRIPTION
---------------------
Before embeddings, vector databases, or LLM calls, a RAG system has to decide
how source documents become retrievable chunks.

Chunking matters because retrieval usually returns chunks, not whole documents.
Chunks that are too large can bury the relevant sentence in unrelated context.
Chunks that are too small can lose the surrounding meaning needed to answer a
question. Overlap is a simple way to reduce meaning lost at chunk boundaries.

Timebox: 45-60 minutes.
Difficulty: A-level beginner/intermediate.

Rules:
- Use only plain Python.
- Do not use LangChain, LlamaIndex, vector databases, embeddings, or LLMs.
- Keep the implementation deterministic and easy to test.
"""

from __future__ import annotations

from typing import TypedDict


# GIVEN / STARTER DATA
STARTER_DOCUMENTS: list[dict[str, str]] = [
    {
        "document_id": "rag-notes",
        "text": (
            "Retrieval augmented generation starts by preparing documents. "
            "Raw files are loaded, normalized, and split into chunks. "
            "Each chunk should preserve enough context to be useful during "
            "retrieval. Metadata helps the system trace an answer back to its "
            "source document."
        ),
    },
    {
        "document_id": "support-policy",
        "text": (
            "Refund requests must include the order id and reason for the "
            "request. Premium accounts receive priority review. Requests older "
            "than thirty days require manager approval."
        ),
    },
]


class ChunkRecord(TypedDict):
    """Output schema for one retrievable chunk."""

    document_id: str
    chunk_index: int
    text: str


# IMPLEMENTATION AREA
def chunk_text(
    *,
    document_id: str,
    text: str,
    chunk_size: int,
    overlap: int = 0,
) -> list[ChunkRecord]:
    """Split one document into chunk records.

    TODO: Implement this function.

    Required behavior:
    - Return [] for empty text.
    - Return one chunk when text is shorter than or equal to chunk_size.
    - Split longer text into approximate character-sized chunks.
    - Support optional character overlap between adjacent chunks.
    - Preserve document_id on every chunk.
    - Set chunk_index to 0, 1, 2, ... in output order.
    - Validate that chunk_size is positive.
    - Validate that overlap is not negative and is smaller than chunk_size.

    Design hint:
    A simple first version can use start/end character offsets:

        start = 0
        end = start + chunk_size
        next_start = end - overlap

    Do not optimize for sentence boundaries yet. That comes later.
    """
    raise NotImplementedError("Implement chunk_text for challenge 001.")


def chunk_documents(
    documents: list[dict[str, str]],
    *,
    chunk_size: int,
    overlap: int = 0,
) -> list[ChunkRecord]:
    """Chunk many starter-style documents into one flat list.

    TODO: Implement this helper after chunk_text works.

    The returned list should preserve document order, and chunk_index should
    restart at 0 for each document.
    """
    raise NotImplementedError("Implement chunk_documents for challenge 001.")


# EXPECTED BEHAVIOR
"""
Example:

    chunk_text(
        document_id="demo",
        text="abcdefghij",
        chunk_size=4,
        overlap=1,
    )

Should return:

    [
        {"document_id": "demo", "chunk_index": 0, "text": "abcd"},
        {"document_id": "demo", "chunk_index": 1, "text": "defg"},
        {"document_id": "demo", "chunk_index": 2, "text": "ghij"},
    ]

The overlap keeps the boundary character from the previous chunk. In a real RAG
pipeline, this helps preserve context when a useful answer spans a boundary.
"""


# SELF-CHECK / TESTS
"""
Run:

    uv run pytest tests/test_001_raw_chunking.py

The tests should fail until you implement the TODOs.
"""


# WRITTEN ANSWERS
"""
After the tests pass, answer these in your own notes:

1. What information could be lost if overlap is always 0?
2. Why should chunk records keep document_id?
3. What is one downside of splitting purely by character count?
4. What chunk_size would you try first for a short FAQ document, and why?
"""
