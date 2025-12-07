# error_replay.py

import os
import json

ERROR_FILE = "./cache/error_replay.jsonl"

def log_error(record):
    os.makedirs("./cache", exist_ok=True)
    with open(ERROR_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def load_errors(limit=10):
    if not os.path.exists(ERROR_FILE):
        return []

    with open(ERROR_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return [json.loads(l) for l in lines][-limit:]
