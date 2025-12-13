import json
from llm.llm_client import call_llm

class Executor:
    def __init__(self, prompt_template):
        self.prompt_template = prompt_template

    def execute(self, question: str, plan: list) -> dict:
        # Combine prompt + plan + question
        formatted_plan = "\n".join([f"{i+1}. {step}" for i, step in enumerate(plan)])
        
        final_prompt = (
            self.prompt_template
            + "\nPLAN:\n"
            + formatted_plan
            + "\n\nQUESTION:\n"
            + question
            + "\n"
        )

        response = call_llm(final_prompt)

        try:
            data = json.loads(response)
            # Must contain intermediate steps + proposed answer
            assert "intermediate" in data
            assert "proposed_answer" in data
            return data

        except Exception as e:
            raise ValueError(f"Executor failed to produce valid JSON: {response}") from e
