import re

def safe_eval_math(text: str):
    """
    Extracts numbers and basic operators for simple arithmetic like:
    - 2+2
    - 10 - 4 + 2
    - 3 * 7
    - 20 / 5
    """

    expr = re.findall(r"[0-9+\-*/ ]+", text)
    if not expr:
        return None

    expr = expr[0].strip()

    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return None
