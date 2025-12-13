import streamlit as st
import json
from main import solve   # your agent pipeline

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Multi-Step Reasoning Agent")
st.write("A production-grade AI that plans → executes → verifies before answering.")

st.divider()

# Input area
question = st.text_area(
    "Enter your question:",
    placeholder="Example: A train leaves at 14:30 and arrives at 18:05. How long is the journey?",
    height=120
)

if st.button("Solve", type="primary"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Working through planner → executor → verifier..."):
            result = solve(question)

        st.subheader("✅ Final Answer")
        st.success(result["answer"])

        st.subheader("📝 High-Level Reasoning (User-Safe)")
        st.info(result["reasoning_visible_to_user"])

        st.divider()

        st.subheader("🔍 Metadata (Debug / Transparency)")
        
        # Plan
        st.markdown("### 📌 Planner Output")
        st.json(result["metadata"].get("plan", {}))

        # Verification logs
        st.markdown("### 🔎 Verifier Checks")
        st.json(result["metadata"].get("checks", {}))

        # Retries
        st.markdown("### 🔁 Retries")
        st.write(result["metadata"].get("retries", 0))

        # Errors only on fail
        if result["status"] == "failed":
            st.error("Agent failed to produce a reliable answer.")
            st.json(result["metadata"].get("error"))
