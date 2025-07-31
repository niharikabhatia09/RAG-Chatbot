import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import pickle

DATA_DIR = "data/"
SAVE_DIR = "faiss_store/"

embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

all_chunks = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DATA_DIR, file))
        documents = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = splitter.split_documents(documents)
        all_chunks.extend(chunks)

vectorstore = FAISS.from_documents(all_chunks, embedding=embedding_model)

# Save vectorstore
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

with open(os.path.join(SAVE_DIR, "index.pkl"), "wb") as f:
    pickle.dump(vectorstore, f)
vectorstore.save_local(SAVE_DIR)
