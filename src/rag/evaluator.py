import time
from typing import List, Dict
from ..utils.logger import get_logger

logger = get_logger(__name__)


class Evaluator:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def evaluate_dataset(self, questions: List[str], ground_truths: List[str]) -> Dict:
        latencies = []
        token_counts = []
        correct = 0
        hallucinations = 0

        for q, gt in zip(questions, ground_truths):
            start = time.time()
            answer, _ = self.pipeline.query(q)
            end = time.time()

            latency_ms = (end - start) * 1000
            latencies.append(latency_ms)

            tokens = len(answer.split())
            token_counts.append(tokens)

            if gt.lower() in answer.lower():
                correct += 1
            else:
                hallucinations += 1

        n = len(questions)
        accuracy = correct / n if n else 0.0
        hallucination_rate = hallucinations / n if n else 0.0
        avg_latency = sum(latencies) / n if n else 0.0
        avg_tokens = sum(token_counts) / n if n else 0.0

        metrics = {
            "accuracy": round(accuracy, 3),
            "avg_latency_ms": round(avg_latency, 2),
            "avg_tokens": round(avg_tokens, 2),
            "hallucination_rate": round(hallucination_rate, 3),
        }

        logger.info("Evaluation metrics: %s", metrics)
        return metrics
