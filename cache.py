# cache.py

import os
import hashlib
import json

CACHE_DIR = "./cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def hash_text(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def path(prefix, text):
    return os.path.join(CACHE_DIR, f"{prefix}_{hash_text(text)}.json")

def load_cache(prefix, key):
    p = path(prefix, key)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_cache(prefix, key, data):
    p = path(prefix, key)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
