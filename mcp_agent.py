from utils import load_thread, save_thread
import requests

def generate_response(context):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",  # Or another model you've pulled (e.g., mistral, phi3)
        "prompt": context,
        "stream": False
    }

    response = requests.post(url, json=payload)
    if response.ok:
        return response.json()["response"].strip()
    else:
        return "Sorry, I couldn't get a response from the model."

def run_agent():
    thread = load_thread()
    print("Previous context:")
    for msg in thread:
        print(f"{msg['role'].capitalize()}: {msg['content']}")

    user_input = input("\nYou: ")
    thread.append({"role": "user", "content": user_input})

    full_context = "\n".join([f"{m['role']}: {m['content']}" for m in thread])
    response = generate_response(full_context)

    print(f"\nAssistant: {response}")
    thread.append({"role": "assistant", "content": response})

    save_thread(thread)

if __name__ == "__main__":
    run_agent()
