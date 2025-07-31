# 📄 LegalDoc AI Chatbot - RAG Pipeline

An AI-powered chatbot using Retrieval-Augmented Generation (RAG) to answer queries from PDFs like Terms, Privacy Policies, or Legal Contracts.

## 🎯 Features
- PDF ingestion + chunking
- Semantic embedding with `bge-small`
- Vector store with FAISS
- Instruction-tuned LLM (Mistral, Falcon, etc.)
- Streamlit chat interface with streaming response

## 🛠 Tech Stack
- Streamlit
- LangChain
- HuggingFace Transformers
- FAISS
- sentence-transformers

## 📦 Setup

```bash
git clone https://github.com/your-username/legal-rag-chatbot.git
cd legal-rag-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
