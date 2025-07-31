from transformers import pipeline

def load_llm():
    return pipeline(
        "text-generation",
        model="mistralai/Mistral-7B-Instruct-v0.1",
        max_new_tokens=512,
        temperature=0.2,
        top_k=50,
        do_sample=True,
        repetition_penalty=1.1
    )
