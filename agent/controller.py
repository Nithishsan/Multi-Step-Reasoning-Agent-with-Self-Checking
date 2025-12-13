import json

class AgentController:
    def __init__(self, planner, executor, verifier, max_retries=0):
        self.planner = planner
        self.executor = executor
        self.verifier = verifier
        self.max_retries = max_retries

    def solve(self, question: str) -> dict:
        retries = 0
        last_error = None
        verification_logs = []

        while retries <= self.max_retries:

            try:
                # 1. PLAN
                plan = self.planner.create_plan(question)

                # 2. EXECUTE
                executor_output = self.executor.execute(question, plan)

                # 3. VERIFY
                verification_result = self.verifier.verify(question, executor_output)

                verification_logs.append(verification_result)

                if verification_result["passed"]:
                    # SUCCESS → return final JSON
                    return {
                        "answer": executor_output["proposed_answer"],
                        "status": "success",
                        "reasoning_visible_to_user": self._summarize(executor_output),
                        "metadata": {
                            "plan": plan,
                            "checks": verification_logs,
                            "retries": retries
                        }
                    }

                else:
                    retries += 1
                    last_error = verification_result["details"]
                    continue  # Retry planner + executor

            except Exception as e:
                last_error = str(e)
                retries += 1
                continue

        # If all retries FAILED → return failure JSON
        return {
            "answer": None,
            "status": "failed",
            "reasoning_visible_to_user": "Unable to produce a reliable answer.",
            "metadata": {
                "plan": None,
                "checks": verification_logs,
                "retries": retries,
                "error": last_error
            }
        }

    def _summarize(self, executor_output):
        """Short user-safe explanation from intermediate steps."""
        steps = executor_output["intermediate"]
        return f"Steps taken: {', '.join(steps)}"
