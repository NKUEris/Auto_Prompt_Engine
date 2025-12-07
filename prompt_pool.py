from dataclasses import dataclass

@dataclass
class PromptEntry:
    prompt: str
    score: float = 0.0

class PromptPool:
    def __init__(self):
        self.pool = []

    def add(self, entry):
        self.pool.append(entry)

    def sort(self):
        self.pool.sort(key=lambda x: x.score, reverse=True)

    def top_k(self, k):
        self.sort()
        return self.pool[:k]

    def sample(self, k):
        self.sort()
        return self.pool[:k]

    def prune(self, max_size):
        self.sort()
        self.pool = self.pool[:max_size]
