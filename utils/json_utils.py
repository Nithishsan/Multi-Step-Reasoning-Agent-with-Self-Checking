import json

def safe_json_loads(raw):
    if not raw:
        return None

    try:
        # If coming from LLM router
        if isinstance(raw, dict) and "content" in raw:
            raw = raw["content"]

        data = json.loads(raw)

        # ✅ ACCEPT BOTH
        if isinstance(data, list):
            return {"steps": data}

        if isinstance(data, dict):
            return data

        return None

    except Exception:
        return None
