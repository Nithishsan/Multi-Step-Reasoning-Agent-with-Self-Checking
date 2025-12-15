import re


def safe_eval_math(text: str):
    """
    Safely evaluates simple arithmetic expressions.
    Supports: +, -, *, /
    Returns int or float, or None if not applicable.
    """

    # Remove spaces
    expr = text.replace(" ", "")

    # Only allow digits and operators
    if not re.fullmatch(r"[0-9+\-*/().]+", expr):
        return None

    try:
        result = eval(expr, {"__builtins__": {}})
    except Exception:
        return None

    # Normalize result
    if isinstance(result, float) and result.is_integer():
        return int(result)

    return result
