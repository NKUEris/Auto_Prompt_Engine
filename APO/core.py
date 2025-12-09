from llm import call_llm
class CritiqueNRefine:
    def __init__(self):
        pass
    def chat_completion(self,context,system_prompt):
       message = [system_prompt,context]
       response = call_llm(message)
       return response
    def critique_n_refine()
        pass
    def mutate(prompt: str, llm) -> str:
        m_prompt = f"""
        以下是一个system prompt，请给它进行小幅改写以提升任务效果：
        {prompt}
        """
        return llm(m_prompt)