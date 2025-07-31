import streamlit as st
from rag_pipeline import get_answer

st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("📄 LegalDoc Chatbot - RAG Based")

query = st.text_input("Ask a question about your documents:")

if query:
    with st.spinner("Thinking..."):
        for chunk in get_answer(query):
            st.write(chunk)
