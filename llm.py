# llm.py
from cache import load_cache, save_cache

def call_llm(system_prompt, dialogue):
    dialogue_text = ""
    for t in dialogue:
        role = t["role"].upper()
        dialogue_text += f"{role}: {t['text']}\n"

    key = system_prompt + "\n" + dialogue_text
    cached = load_cache("gen", key)
    if cached:
        return cached["response"]

    # TODO: 替换为真实模型调用
    response = f"[SIMULATED]\n{dialogue_text}"

    save_cache("gen", key, {"response": response})
    return response
