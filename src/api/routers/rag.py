from fastapi import APIRouter, HTTPException
from ..models.request_response import QueryRequest, QueryResponse, EvalRequest, EvalResponse
from ...rag.pipeline import RAGPipeline
from ...rag.evaluator import Evaluator

router = APIRouter()
pipeline = RAGPipeline()
evaluator = Evaluator(pipeline=pipeline)


@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    try:
        answer, retrieved_docs = pipeline.query(request.question, top_k=request.top_k)
        return QueryResponse(
            question=request.question,
            answer=answer,
            retrieved_documents=retrieved_docs,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/evaluate", response_model=EvalResponse)
def evaluate_rag(request: EvalRequest):
    try:
        metrics = evaluator.evaluate_dataset(
            questions=request.questions,
            ground_truths=request.ground_truths,
        )
        return EvalResponse(**metrics)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
