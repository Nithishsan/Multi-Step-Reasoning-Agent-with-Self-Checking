# =========================
# Planner Prompt
# =========================

PLANNER_PROMPT = """
You are the Planner component of a multi-step reasoning agent.

Your task:
- Read the question carefully
- Break it into clear, logical steps
- Output ONLY valid JSON
- Do NOT include explanations or extra text

Output format (JSON array of strings):

[
  "Step 1 description",
  "Step 2 description",
  "Step 3 description"
]

Example:
Question: "Alice has 3 apples and buys 2 more."
Output:
[
  "Identify the initial number of apples",
  "Identify the number of apples bought",
  "Add both quantities to get the final total"
]

Now generate a plan for this question:
"{question}"
"""


# =========================
# Executor Prompt
# =========================

EXECUTOR_PROMPT = """
You are the Executor component.

Follow the given plan step-by-step and compute the answer.

Rules:
- Execute each step logically
- Show intermediate results
- Output ONLY valid JSON
- Do NOT include explanations outside JSON

Return JSON in the following format:
{{
  "steps_executed": [
    {{"step": "Step description", "result": "Intermediate result"}}
  ],
  "final_answer": "Final answer in natural language"
}}

Example:
{{
  "steps_executed": [
    {{"step": "Initial apples", "result": "3"}},
    {{"step": "Apples bought", "result": "2"}},
    {{"step": "Total apples", "result": "5"}}
  ],
  "final_answer": "Alice has 5 apples."
}}

Question:
"{question}"

Plan:
{plan}
"""


# =========================
# Verifier Prompt (Not used by rule-based verifier, kept for completeness)
# =========================

VERIFIER_PROMPT = """
You are the Verifier component.

Your task:
- Independently check if the final answer is correct
- Be strict and logical
- Output ONLY valid JSON

Return JSON in this format:
{{
  "passed": true,
  "details": "Short explanation of verification"
}}

Example:
{{
  "passed": true,
  "details": "Recalculation confirms the result is correct."
}}

Question:
"{question}"

Proposed Answer:
"{answer}"
"""
