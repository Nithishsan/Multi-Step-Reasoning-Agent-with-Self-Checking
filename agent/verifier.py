import re
from utils.math_utils import safe_eval_math
from utils.time_utils import compute_time_difference


class Verifier:
    """
    Rule-based verifier.
    No LLM calls → zero cost, zero rate limits.
    """

    def __init__(self):
        self.name = "RuleBasedVerifier"

    def verify(self, question: str, answer: str) -> dict:
        """
        Verifies the answer using deterministic logic when possible.
        Falls back to pass=True if verification is not applicable.
        """

        # ---- Time problems ----
        if "leaves at" in question and "arrives at" in question:
            expected = compute_time_difference(question)
            return {
                "passed": expected.lower() in answer.lower(),
                "details": f"Expected duration: {expected}"
            }

        # ---- Simple arithmetic problems ----
        numbers = list(map(int, re.findall(r"\d+", question)))
        if numbers:
            expected = safe_eval_math(question)
            if expected is not None:
                return {
                    "passed": str(expected) in answer,
                    "details": f"Expected numeric result: {expected}"
                }

        # ---- Default fallback ----
        return {
            "passed": True,
            "details": "No deterministic rule applied; accepted by default."
        }
