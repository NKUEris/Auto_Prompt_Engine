# evaluator.py

from llm import call_llm
from judge import judge
from error_replay import log_error

def evaluate_prompt(system_prompt, eval_data, round_id=0):
    total = 0
    score = 0.0

    for item in eval_data:
        dialogue = item["dialogue"]
        expected = item.get("expected_behavior", "")

        assistant_output = call_llm(system_prompt, dialogue)
        s = judge(system_prompt, dialogue, assistant_output)

        if s < 6.0:
            log_error({
                "system_prompt": system_prompt,
                "dialogue": dialogue,
                "assistant_output": assistant_output,
                "judge_score": s,
                "expected_behavior": expected,
                "round": round_id
            })

        score += s
        total += 1

    return score / total
