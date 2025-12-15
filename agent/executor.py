import json
from llm.llm_client import call_llm
from agent.prompts import EXECUTOR_PROMPT


class Executor:
    def __init__(self):
        self.name = "Executor"

    def execute(self, question: str, plan: list) -> str:
        prompt = f"""
{EXECUTOR_PROMPT}

Question:
"{question}"

Plan:
{json.dumps(plan, ensure_ascii=False)}
"""
        return call_llm(prompt)
