import json
import re


def safe_json_loads(text: str):
    """
    Attempts to safely parse JSON from LLM output.
    Handles extra text before/after JSON.
    """
    if not text:
        return None

    # First try direct parse
    try:
        return json.loads(text)
    except Exception:
        pass

    # Fallback: extract JSON substring
    match = re.search(r'(\{[\s\S]*\}|\[[\s\S]*\])', text)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            return None

    return None
