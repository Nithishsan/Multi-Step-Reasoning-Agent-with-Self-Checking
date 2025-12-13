import json
from llm.llm_client import call_llm

class Verifier:
    def __init__(self, prompt_template):
        self.prompt_template = prompt_template

    def verify(self, question: str, executor_output: dict) -> dict:
        proposed = executor_output["proposed_answer"]
        intermediates = executor_output["intermediate"]

        final_prompt = (
            self.prompt_template
            + "\nQUESTION:\n"
            + question
            + "\n\nEXECUTOR OUTPUT:\n"
            + json.dumps(executor_output, indent=2)
            + "\n"
        )

        response = call_llm(final_prompt)

        try:
            data = json.loads(response)
            if "passed" not in data or "details" not in data:
               raise ValueError("Missing keys")
            return data

        except Exception:
        # SAFETY NET: never crash the agent
            return {
                "passed": False,
                "details": "Verifier returned invalid JSON output."
    }
