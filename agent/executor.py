import json
from llm.llm_client import call_llm
from agent.prompts import EXECUTOR_PROMPT


class Executor:
    """
    Executor component responsible for executing
    the reasoning plan step-by-step and producing
    a final answer.
    """

    def __init__(self):
        self.name = "Executor"

    def _build_prompt(self, question: str, plan: list) -> str:
        """
        Builds the executor prompt using the plan and question.
        """
        return EXECUTOR_PROMPT.format(
            question=question,
            plan=json.dumps(plan, ensure_ascii=False)
        )

    def execute(self, question: str, plan: list) -> str:
        """
        Executes the reasoning plan.

        Returns:
            Raw JSON string containing final_answer
        """
        if not question or not plan:
            raise ValueError("Executor received invalid inputs.")

        prompt = self._build_prompt(question, plan)

        # 🔹 UPDATED: call_llm now returns a dict
        response = call_llm(prompt)

        if not response or "content" not in response:
            raise RuntimeError("Executor received invalid LLM response.")

        return response["content"]
