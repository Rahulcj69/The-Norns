import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_gemma(prompt):
    response=requests.post(
        OLLAMA_URL,
        json={
            "model": "gemma4:e2b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]