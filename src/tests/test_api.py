from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_query():
    payload = {"question": "What is RAG?", "top_k": 2}
    resp = client.post("/rag/query", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "answer" in data
    assert "retrieved_documents" in data
