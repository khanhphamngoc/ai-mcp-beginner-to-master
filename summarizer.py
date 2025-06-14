import json
import requests
from datetime import datetime
from utils import load_thread, save_summary

def run_agent(model="llama3"):
    thread = load_thread()
    context = "\n".join([f"{m['role']}: {m['content']}" for m in thread])

    prompt = f"Summarize this conversation briefly but meaningfully:\n{context}"

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if response.ok:
        summary = response.json()["response"].strip()
        save_summary(summary)
        print("\n📝 Thread summary:\n", summary)
    else:
        print("Failed to summarize thread.")

if __name__ == "__main__":
    run_agent()
