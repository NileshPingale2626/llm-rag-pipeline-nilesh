import faiss
import numpy as np
from typing import List, Tuple


class Retriever:
    def __init__(self, dim: int = 384):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.documents: List[str] = []
        self.embeddings = None

    def build_index(self, embeddings: np.ndarray, docs: List[str]):
        self.embeddings = embeddings.astype("float32")
        self.index.add(self.embeddings)
        self.documents = docs

    def search(self, query_embedding: np.ndarray, top_k: int = 3) -> List[Tuple[str, float]]:
        if self.index.ntotal == 0:
            return []

        query_embedding = query_embedding.astype("float32")
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx < 0 or idx >= len(self.documents):
                continue
            results.append((self.documents[idx], float(dist)))
        return results
