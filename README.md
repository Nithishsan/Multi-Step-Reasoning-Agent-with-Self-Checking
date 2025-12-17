# 🧠 Multi-Step Reasoning Agent with Self-Checking

A **production-grade AI reasoning agent** that solves structured problems by **planning**, **executing**, and **verifying** its own answers before responding.

This project demonstrates how to build a **reliable, self-correcting LLM-based agent** that avoids hallucination by enforcing structured reasoning and verification loops.

---

## 🚀 Key Features

- ✅ **Multi-step reasoning pipeline**
- 🧩 **Planner → Executor → Verifier architecture**
- 🔁 **Automatic retry on verification failure**
- 🛡️ **No chain-of-thought leakage**
- 📦 **Clean JSON-based outputs**
- 🧪 **Unit tests + performance tests**
- 🖥️ **CLI & Streamlit UI**
- ⚙️ **Git LFS–ready repository**

---

## 🏗️ Architecture Overview

      User Question
           ↓
        Planner
     (creates plan)
           ↓
        Executor
     (follows plan)
           ↓
        Verifier
    (independent check)
           ↓
      Controller Loop
     (retry if needed)
            ↓
      Final Answer

### Components

| Module | Responsibility |
|------|---------------|
| Planner | Converts a question into a structured, step-by-step plan |
| Executor | Executes the plan and computes the solution |
| Verifier | Independently re-solves and validates correctness |
| Controller | Orchestrates retries and final output |
| LLM Client | Abstracts the LLM provider (OpenAI) |      

## 📂 Project Structure
📦 Multi-Step-Reasoning-Agent-with-Self-Checking
│
├── 📁 agent
│   ├── 📄 __init__.py
│   ├── 📄 controller.py
│   ├── 📄 planner.py
│   ├── 📄 executor.py
│   └── 📄 prompts.py
│
├── 📁 llm
│   ├── 📄 __init__.py
│   └── 📄 llm_client.py
│
├── 📁 utils
│   ├── 📄 __init__.py
│   ├── 📄 math_utils.py
│   ├── 📄 time_utils.py
│   ├── 📄 scheduling_utils.py
│   └── 📄 logger.py
│
├── 📁 tests
│   └── 📄 test_agent.py
│
├── 📄 streamlit_app.py
├── 📄 main.py
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md


---

## 🧠 Problem Types Supported

- Arithmetic & word problems
- Time calculations (including next-day rollovers)
- Constraint-based scheduling
- Multi-step logical reasoning
- Unit conversions
- Edge-case validation

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **OpenAI API**
- **Streamlit** (UI)
- **PyTest** (testing)
- **Git LFS** (large file handling)
---
## 🔐 Environment Setup

### 1️⃣ Create Virtual Environment

python -m venv .venv
Activate:

Windows
.venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set OpenAI API Key
export OPENAI_API_KEY="your_api_key_here"

(Windows PowerShell)
$env:OPENAI_API_KEY="your_api_key_here"

▶️ Running the Project
🔹 CLI Mode
python main.py

Example:
A train leaves at 14:30 and arrives at 18:05. How long is the journey?

🔹 Streamlit UI
streamlit run app.py

