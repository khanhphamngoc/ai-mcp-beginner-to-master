import json
from datetime import datetime

def load_thread(filename="thread_store.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_thread(thread, filename="thread_store.json"):
    with open(filename, "w") as f:
        json.dump(thread,f,indent=2)

def save_summary(summary, filename="summary_store.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"summaries": []}

    new_entry = {
        "id": f"session-{len(data['summaries']) + 1}",
        "summary": summary,
        "timestamp": datetime.now().isoformat()
    }

    data["summaries"].append(new_entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)