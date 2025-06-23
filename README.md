# 🔍 AI Job Dataset Q&A System

A local Retrieval-Augmented Generation (RAG) application built using **LangChain**, **Ollama**, and **ChromaDB** that answers questions from a dataset of AI job listings.

## 📌 Project Overview

This project allows users to ask natural language questions about AI-related jobs, and get accurate answers based on real job listings. It uses:

- 🧠 **Ollama LLM (LLaMA3)** for generating intelligent responses.
- 📚 **Chroma Vector Store** for storing and retrieving semantically relevant job listings.
- 🔎 **LangChain** to connect embeddings, retrieval, and the LLM in a seamless pipeline.

---

## 📂 Dataset Used

The project uses a CSV dataset named: `ai_job_dataset.csv`.

Sample columns expected:
- `Job Title`
- `Company`
- `Description`
- `Location` *(optional)*
- `Salary` *(optional)*

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash

cd ai-job-rag-system](https://github.com/akashsingh62/ollama-ollama-agent-project-demo)
