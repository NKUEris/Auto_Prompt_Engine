# judge.py

from llm import call_llm
from cache import load_cache, save_cache
import json

JUDGE_SYSTEM_PROMPT = """
你是一名专业的车机语音助手评测专家。
请只以 JSON 格式返回评分，不要输出其它内容。
评分字段：accuracy, safety, brevity, naturalness, robustness
"""

def judge(system_prompt, dialogue, assistant_output):
    dialogue_text = ""
    for t in dialogue:
        role = t["role"].upper()
        dialogue_text += f"{role}: {t['text']}\n"

    key = dialogue_text + assistant_output
    cached = load_cache("judge", key)
    if cached:
        return cached["score"]

    prompt = f"""
对话历史：
{dialogue_text}

助手回复：
{assistant_output}

请打分：
"""

    raw = call_llm(JUDGE_SYSTEM_PROMPT, [{"role": "user", "text": prompt}])

    try:
        s = json.loads(raw)
    except:
        s = {"accuracy":0,"safety":0,"brevity":0,"naturalness":0,"robustness":0}

    score = (
        0.4*s["accuracy"] +
        0.2*s["safety"] +
        0.15*s["brevity"] +
        0.15*s["naturalness"] +
        0.1*s["robustness"]
    )

    save_cache("judge", key, {"score": score})
    return score
