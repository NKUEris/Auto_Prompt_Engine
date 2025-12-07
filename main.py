# main.py

from config import *
from prompt_pool import *
from mutator import mutate_system_prompt
from evaluator import evaluate_prompt
import json

def load_eval():
    with open("data/eval_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    eval_data = load_eval()
    pool = PromptPool()

    pool.add(PromptEntry(BASE_SYSTEM_PROMPT))

    for _ in range(INIT_VARIANTS):
        pool.add(PromptEntry(mutate_system_prompt(BASE_SYSTEM_PROMPT)))

    pool.prune(MAX_POOL_SIZE)

    for r in range(ROUNDS):
        print(f"=== ROUND {r} ===")

        for entry in pool.sample(SAMPLED_PER_ROUND):
            entry.score = evaluate_prompt(entry.prompt, eval_data, r)

        parents = pool.top_k(TOP_K)

        for p in parents:
            pool.add(PromptEntry(mutate_system_prompt(p.prompt)))

        pool.prune(MAX_POOL_SIZE)

    best = pool.top_k(1)[0]
    print("\nBEST PROMPT:\n")
    print(best.prompt)

if __name__ == "__main__":
    main()
