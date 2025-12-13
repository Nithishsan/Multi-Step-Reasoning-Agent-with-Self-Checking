import json
from llm.llm_client import call_llm


class Planner:
    def __init__(self, prompt_template: str):
        self.prompt_template = prompt_template

    def create_plan(self, question: str) -> list:
        prompt = (
            self.prompt_template
            + "\nQUESTION:\n"
            + question
            + "\n"
        )

        response = call_llm(prompt)

        try:
           data = json.loads(response)
           plan = data.get("plan")

           if not isinstance(plan, list):
               raise ValueError("Invalid plan structure")

           return plan

        except Exception:
        # SAFETY: Planner must never crash the agent
           return None
