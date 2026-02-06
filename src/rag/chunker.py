from typing import List


def chunk_text(text: str, max_tokens: int = 200) -> List[str]:
    # Simple whitespace-based chunking for demo
    words = text.split()
    chunks = []
    current = []

    for w in words:
        current.append(w)
        if len(current) >= max_tokens:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks
