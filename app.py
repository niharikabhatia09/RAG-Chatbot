import streamlit as st

# Hardcoded demo Q&A pairs
demo_qa = {
    "what is an nda": "An NDA, or Non-Disclosure Agreement, is a legal contract that establishes a confidential relationship.",
    "when does the contract expire": "The contract expires 12 months from the effective date.",
    "what are the arbitration terms": "Arbitration will be conducted in New Delhi under Indian law.",
    "can i use this template in germany": "This contract is governed by Indian law. Use in other jurisdictions should be reviewed by local counsel.",
    "what is the president’s name": "I’m not sure. This is outside the scope of the document."
}

# Simple answer function
def get_answer(query):
    cleaned_query = query.lower().strip()
    return demo_qa.get(cleaned_query, "I'm sorry, I don't have information on that yet.")

# Streamlit app layout
st.set_page_config(page_title="AI Chatbot Demo", layout="wide")
st.title("📄 LegalDoc Chatbot – Demo Version")

query = st.text_input("Ask a question:")

if query:
    with st.spinner("Thinking..."):
        answer = get_answer(query)
        st.write("💬 " + answer)
