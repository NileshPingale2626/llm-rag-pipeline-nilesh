from fastapi import FastAPI
from .routers import rag

app = FastAPI(
    title="LLM RAG API",
    description="LLM-powered Retrieval-Augmented Generation pipeline by Nilesh Pingale",
    version="0.1.0",
)

app.include_router(rag.router, prefix="/rag", tags=["RAG"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
