class ToolAgent:
    """
    Placeholder for an agent that could orchestrate tools:
    - RAG pipeline
    - External APIs
    - Calculators, etc.
    """

    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline

    def handle_query(self, query: str) -> str:
        answer, _ = self.rag_pipeline.query(query)
        return answer
