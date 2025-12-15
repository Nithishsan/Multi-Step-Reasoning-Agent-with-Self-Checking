from llm.llm_client import call_llm
from agent.prompts import PLANNER_PROMPT


class Planner:
    """
    Planner component responsible for decomposing
    a user question into a structured reasoning plan.

    Output is expected to be a JSON array of step strings.
    """

    def __init__(self):
        self.name = "Planner"

    def _build_prompt(self, question: str) -> str:
        """
        Constructs the planner prompt using the shared template.
        """
        return PLANNER_PROMPT.format(question=question)

    def plan(self, question: str) -> str:
        """
        Generates a reasoning plan for the given question.

        Returns:
            Raw LLM output (JSON list of steps)
        """
        if not question or not question.strip():
            raise ValueError("Planner received an empty question.")

        prompt = self._build_prompt(question)
        response = call_llm(prompt)

        if not response:
            raise RuntimeError("Planner received empty response from LLM.")

        return response
