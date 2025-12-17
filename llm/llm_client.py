import os
import time
from dotenv import load_dotenv
from utils.logger import get_logger

# ✅ Load environment variables FIRST
load_dotenv()

from openai import OpenAI
from groq import Groq

logger = get_logger("LLMRouter")

OPENAI_MODEL = "gpt-4o-mini"
GROQ_MODEL = "llama-3.3-70b-versatile"


def _get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)


def _get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")
    return Groq(api_key=api_key)


def call_llm(prompt: str) -> dict:
    """
    Unified LLM router:
    1. Try OpenAI
    2. Fallback to Groq
    """

    if not prompt or not prompt.strip():
        raise ValueError("Empty prompt sent to LLM")

    # ---------- TRY OPENAI ----------
    try:
        logger.info("Trying OpenAI")
        start = time.time()

        openai_client = _get_openai_client()
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=500,
        )

        latency = round(time.time() - start, 3)
        content = response.choices[0].message.content.strip()

        logger.info(f"OpenAI success ({latency}s)")
        return {
            "content": content,
            "provider": "OpenAI",
            "latency": latency,
        }

    except Exception as e:
        logger.warning(f"OpenAI failed → fallback to Groq | {e}")

    # ---------- TRY GROQ ----------
    try:
        logger.info("Trying Groq")
        start = time.time()

        groq_client = _get_groq_client()
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=500,
        )

        latency = round(time.time() - start, 3)
        content = response.choices[0].message.content.strip()

        logger.info(f"Groq success ({latency}s)")
        return {
            "content": content,
            "provider": "Groq",
            "latency": latency,
        }

    except Exception as e:
        logger.error(f"Groq failed | {e}")
        raise RuntimeError("All LLM providers failed")
