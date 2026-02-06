from typing import List, Tuple
import numpy as np
from .chunker import chunk_text
from .embedder import Embedder
from .retriever import Retriever
from ..utils.logger import get_logger

logger = get_logger(__name__)


class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.retriever = Retriever()
        self._initialized = False

    def _initialize_corpus(self):
        # For demo: static corpus; in real use, load from data/processed
        docs = [
            "SAP CPQ is a configure-price-quote solution for complex product offerings.",
            "RAG stands for Retrieval-Augmented Generation, combining search with LLMs.",
            "MLOps focuses on operationalizing machine learning models in production.",
        ]
        chunks = []
        for d in docs:
            chunks.extend(chunk_text(d, max_tokens=50))

        embeddings = self.embedder.encode(chunks)
        self.retriever.build_index(embeddings, chunks)
        self._initialized = True
        logger.info("RAG corpus initialized with %d chunks", len(chunks))

    def query(self, question: str, top_k: int = 3) -> Tuple[str, List[str]]:
        if not self._initialized:
            self._initialize_corpus()

        q_emb = self.embedder.encode([question])
        results = self.retriever.search(q_emb, top_k=top_k)
        retrieved_docs = [r[0] for r in results]
        answer = self.embedder.llm_answer(question, retrieved_docs)
        return answer, retrieved_docs
