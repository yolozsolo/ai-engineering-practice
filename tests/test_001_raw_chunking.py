from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest


def load_challenge() -> ModuleType:
    challenge_path = (
        Path(__file__).resolve().parents[1] / "challenges" / "001_raw_chunking.py"
    )
    spec = importlib.util.spec_from_file_location("challenge_001_raw_chunking", challenge_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


challenge = load_challenge()


def test_short_text_returns_single_chunk_with_metadata() -> None:
    chunks = challenge.chunk_text(
        document_id="doc-1",
        text="short note",
        chunk_size=50,
    )

    assert chunks == [
        {
            "document_id": "doc-1",
            "chunk_index": 0,
            "text": "short note",
        }
    ]


def test_empty_text_returns_no_chunks() -> None:
    chunks = challenge.chunk_text(
        document_id="empty-doc",
        text="",
        chunk_size=10,
    )

    assert chunks == []


def test_splits_text_by_approximate_character_size_without_overlap() -> None:
    chunks = challenge.chunk_text(
        document_id="letters",
        text="abcdefghij",
        chunk_size=4,
    )

    assert chunks == [
        {"document_id": "letters", "chunk_index": 0, "text": "abcd"},
        {"document_id": "letters", "chunk_index": 1, "text": "efgh"},
        {"document_id": "letters", "chunk_index": 2, "text": "ij"},
    ]


def test_splits_text_with_overlap_between_adjacent_chunks() -> None:
    chunks = challenge.chunk_text(
        document_id="letters",
        text="abcdefghij",
        chunk_size=4,
        overlap=1,
    )

    assert chunks == [
        {"document_id": "letters", "chunk_index": 0, "text": "abcd"},
        {"document_id": "letters", "chunk_index": 1, "text": "defg"},
        {"document_id": "letters", "chunk_index": 2, "text": "ghij"},
    ]


def test_chunk_documents_preserves_document_order_and_resets_index() -> None:
    documents = [
        {"document_id": "a", "text": "abcdef"},
        {"document_id": "b", "text": "wxyz"},
    ]

    chunks = challenge.chunk_documents(documents, chunk_size=3)

    assert chunks == [
        {"document_id": "a", "chunk_index": 0, "text": "abc"},
        {"document_id": "a", "chunk_index": 1, "text": "def"},
        {"document_id": "b", "chunk_index": 0, "text": "wxy"},
        {"document_id": "b", "chunk_index": 1, "text": "z"},
    ]


@pytest.mark.parametrize(
    ("chunk_size", "overlap"),
    [
        (0, 0),
        (-1, 0),
        (5, -1),
        (5, 5),
        (5, 6),
    ],
)
def test_rejects_invalid_chunk_settings(chunk_size: int, overlap: int) -> None:
    with pytest.raises(ValueError):
        challenge.chunk_text(
            document_id="bad-settings",
            text="abcdef",
            chunk_size=chunk_size,
            overlap=overlap,
        )
