from llm.llm_client import call_llm
from agent.prompts import PLANNER_PROMPT
import json


class Planner:
    """
    Planner component responsible for converting
    a user question into a structured reasoning plan.

    Output format (expected JSON):
    {
        "steps": [
            "Step 1 ...",
            "Step 2 ..."
        ]
    }
    """

    def __init__(self):
        self.name = "Planner"

    def _build_prompt(self, question: str) -> str:
        """
        Builds the planner prompt using a shared template.
        """
        return PLANNER_PROMPT.format(question=question.strip())

    def _fallback_plan(self, question: str) -> dict:
        """
        Deterministic fallback if LLM fails or returns bad output.
        This prevents total pipeline failure.
        """
        return {
            "steps": [
                f"Understand the problem: {question}",
                "Apply logical reasoning or calculations",
                "Produce the final answer clearly"
            ]
        }

    def plan(self, question: str) -> str:
        """
        Generates a reasoning plan for the given question.

        Returns:
            JSON string representing a reasoning plan
        """
        if not question or not question.strip():
            return json.dumps(self._fallback_plan("Unknown question"))

        prompt = self._build_prompt(question)

        try:
            response = call_llm(prompt)
            if not response:
                return json.dumps(self._fallback_plan(question))
            return response

        except Exception:
            # Absolute safety: NEVER let planner crash the agent
            return json.dumps(self._fallback_plan(question))
