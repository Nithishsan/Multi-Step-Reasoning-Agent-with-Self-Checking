from agent.planner import Planner
from agent.executor import Executor
from agent.verifier import Verifier

from utils.json_utils import safe_json_loads
from utils.math_utils import safe_eval_math
from utils.time_utils import compute_time_difference
from utils.scheduling_utils import find_fitting_slots

import re


class AgentController:
    """
    Central controller for the Multi-Step Reasoning Agent.

    Flow priority:
    1. Deterministic math problems (NO LLM)
    2. Deterministic time-difference problems (NO LLM)
    3. Deterministic scheduling / meeting-slot problems (NO LLM)
    4. LLM-based Planner → Executor → Verifier pipeline
    """

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.verifier = Verifier()

    def solve(self, question: str) -> dict:
        if not question or not question.strip():
            return self._fail("Empty question received.", None)

        question = question.strip()

        # =====================================================
        # FAST PATH 1 — SIMPLE MATH (NO LLM)
        # =====================================================
        math_result = safe_eval_math(question)
        if math_result is not None:
            return {
                "status": "success",
                "answer": str(math_result),
                "reasoning": "Solved deterministically (math_utils)",
                "metadata": {"source": "math_utils"}
            }

        # =====================================================
        # FAST PATH 2 — TIME DIFFERENCE (NO LLM)
        # =====================================================
        if "leaves at" in question.lower() and "arrives at" in question.lower():
            duration = compute_time_difference(question)
            if duration:
                return {
                    "status": "success",
                    "answer": duration,
                    "reasoning": "Solved deterministically (time_utils)",
                    "metadata": {"source": "time_utils"}
                }

        # =====================================================
        # FAST PATH 3 — MEETING / SCHEDULING PROBLEMS (NO LLM)
        # =====================================================
        if "meeting" in question.lower() and "slot" in question.lower():
            slots = find_fitting_slots(question, required_minutes=60)
            if slots:
                return {
                    "status": "success",
                    "answer": ", ".join(slots),
                    "reasoning": "Solved deterministically (scheduling_utils)",
                    "metadata": {"source": "scheduling_utils"}
                }

        # =====================================================
        # SLOW PATH — LLM PIPELINE
        # =====================================================

        # ---------- Step 1: Planner ----------
        raw_plan = self.planner.plan(question)
        plan = safe_json_loads(raw_plan)

        if not plan:
            return self._fail("Planner failed to produce valid JSON.", raw_plan)

        # ---------- Step 2: Executor ----------
        raw_exec = self.executor.execute(question, plan)
        exec_result = safe_json_loads(raw_exec)

        if not exec_result or "final_answer" not in exec_result:
            return self._fail("Executor failed to produce valid JSON.", raw_exec)

        final_answer = exec_result["final_answer"]

        # ---------- Step 3: Verifier ----------
        verification = self.verifier.verify(question, final_answer)

        if not verification.get("passed", False):
            return self._fail("Verification failed.", verification)

        # ---------- SUCCESS ----------
        return {
            "status": "success",
            "answer": final_answer,
            "reasoning": exec_result,
            "metadata": {
                "plan": plan,
                "verification": verification,
                "source": "LLM + rules"
            }
        }

    def _fail(self, reason: str, raw_output):
        return {
            "status": "failed",
            "answer": None,
            "error": reason,
            "raw_output": raw_output
        }
