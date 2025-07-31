from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from load_model import load_llm
import pickle
import os

embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

# Load FAISS index
if not os.path.exists("faiss_store/index.faiss"):
    raise FileNotFoundError("FAISS vectorstore not found. Run embed_documents.py first.")

with open("faiss_store/index.pkl", "rb") as f:
    vectorstore = pickle.load(f)

llm = load_llm()

def get_answer(query):
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""You are a helpful legal assistant. Use the context to answer the question.
If the answer is not found in the context, say 'I don't know based on the given documents.'

Context:
{context}

Question: {query}
Answer:"""

    response = llm(prompt)
    yield response
