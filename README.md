# 🧠 LLM RAG Agent Demo – Health Use Case

This is a simple demo of a **Retrieval-Augmented Generation (RAG)** agent using OpenAI and FAISS to answer medical-related questions.

## ✅ Features

- Loads a basic health knowledge base (`medical_notes.txt`)
- Splits and embeds content using OpenAI Embeddings
- Stores in FAISS Vector DB
- Answers user questions using GPT-3.5 and `RetrievalQA` from LangChain
- Ready to scale into more advanced agentic workflows

---

## 💻 Stack

- Python 3.12
- OpenAI (ChatGPT API)
- FAISS (in-memory vector store)
- LangChain (retrieval pipeline)
- `.env` support for OpenAI key

---

## 🚀 Quickstart

```bash
git clone https://github.com/Dimitrios79/llm-rag-agent-demo.git
cd llm-rag-agent-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
