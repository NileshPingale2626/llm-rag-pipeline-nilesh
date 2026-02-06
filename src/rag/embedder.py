from sentence_transformers import SentenceTransformer
import numpy as np


class Embedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings

    def llm_answer(self, question: str, docs: list[str]) -> str:
        # Placeholder: in real project, call OpenAI / HF LLM
        # Here we just concatenate docs and pretend it's an answer
        context = "\n".join(docs)
        return f"Answer based on retrieved context:\n{context[:800]}"
