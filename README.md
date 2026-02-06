# LLM-Powered RAG Pipeline – Nilesh Pingale

This repository contains a complete Retrieval-Augmented Generation (RAG) system built as part of my MSc in Data Science & AI at DSTI Paris.  
It demonstrates practical experience in:

- LLM-powered pipelines  
- Embeddings & vector search  
- Retrieval systems (FAISS / ChromaDB)  
- Backend API development (FastAPI)  
- CI/CD automation  
- Docker containerization  
- Evaluation metrics (latency, hallucination, cost)  
- Agent/tool integrations (LangChain)  

This project is designed to reflect real-world AI engineering workflows used in production environments.

---

##  Features

### LLM Components
- Document chunking & preprocessing  
- Embedding generation (Hugging Face / OpenAI)  
- Vector indexing (FAISS or ChromaDB)  
- Retrieval pipeline  
- LLM response generation  
- Evaluation harness for:
  - Hallucination rate  
  - Latency  
  - Token cost  
  - Accuracy  

###  Backend API (FastAPI)
- `/query` endpoint for RAG responses  
- `/evaluate` endpoint for automated testing  
- `/health` endpoint for monitoring  

### MLOps & CI/CD
- GitHub Actions workflow for:
  - Linting  
  - Unit tests  
  - Docker build  
  - Deployment pipeline  

###  Docker & Deployment
- Dockerfile for reproducible builds  
- docker-compose for local vector DB + API  

###  Agents & Tools
- LangChain-based tool agent  
- Retrieval + LLM + tool orchestration  

---

##  Project Structure

(Include the folder structure from above)

---

## Running Locally

