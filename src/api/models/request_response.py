from pydantic import BaseModel
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


class QueryResponse(BaseModel):
    question: str
    answer: str
    retrieved_documents: List[str]


class EvalRequest(BaseModel):
    questions: List[str]
    ground_truths: List[str]


class EvalResponse(BaseModel):
    accuracy: float
    avg_latency_ms: float
    avg_tokens: float
    hallucination_rate: float
