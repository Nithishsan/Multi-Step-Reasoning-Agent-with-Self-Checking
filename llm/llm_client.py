import os
from openai import OpenAI

# Load key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set.")

client = OpenAI(api_key=OPENAI_API_KEY)


def call_llm(prompt: str,
             model: str = "gpt-4o-mini",
             temperature: float = 0.0) -> str:
    """
    Wrapper for OpenAI ChatCompletion API (v1.x SDK).
    Returns plain text output from the model.
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )

        # NEW SDK FORMAT:
        # response.choices[0].message is NOT a dict
        # It uses attributes, not subscriptable keys
        
        return response.choices[0].message.content

    except Exception as e:
        raise RuntimeError(f"LLM call failed: {e}")
