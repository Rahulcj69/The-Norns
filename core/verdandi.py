from core.gemma import ask_gemma

def handle_query(question):

    prompt=f"""
You are Verdandi, an AI tutor.

Rules:
- Explain clearly and simply
- Do NOT show thinking steps, only final answer
- Do Not write "thinking" or "analysis"
- Keep answers short and clean
- Use examples if needed

Question: {question}
"""
    
    response = ask_gemma(prompt)
    return response