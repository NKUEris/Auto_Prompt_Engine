# mutator.py

from llm import call_llm
from error_replay import load_errors

def mutate_system_prompt(prompt):
    errors = load_errors(10)

    error_text = ""
    for e in errors:
        error_text += f"""
对话：
{e['dialogue']}
错误回复：
{e['assistant_output']}
期望：
{e['expected_behavior']}
"""

    meta = f"""
你是车机语音助手的Prompt工程专家。

当前 prompt:
{prompt}

历史错误：
{error_text}

请优化该 system prompt，使其避免这些错误。
只返回新的 system prompt。
"""

    return call_llm("", [{"role":"user","text":meta}])
