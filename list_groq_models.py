from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("\n🔍 Available Models for Your Groq API Key:\n")

models = client.models.list()

for m in models.data:
    print("-", m.id)
