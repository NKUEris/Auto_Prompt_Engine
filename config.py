# config.py

BASE_SYSTEM_PROMPT = """
你是一名车机智能语音助手，负责帮助驾驶员安全完成车内操作。
你必须优先保证驾驶安全，回答简洁，不打断驾驶注意力。
"""

MAX_POOL_SIZE = 10
INIT_VARIANTS = 5
ROUNDS = 10
SAMPLED_PER_ROUND = 5
TOP_K = 3

JUDGE_THRESHOLD = 6.0
