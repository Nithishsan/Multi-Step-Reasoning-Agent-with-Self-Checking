import streamlit as st
from agent.controller import AgentController
import time

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🧠 Multi-Step Reasoning Agent")
st.caption(
    "A hybrid AI system that plans → executes → verifies before answering.\n\n"
    "• Deterministic logic for math & time\n"
    "• OpenAI with Groq fallback for reasoning\n"
    "• Built for reliability, not demos"
)

st.divider()

# -------------------------------------------------
# Controller
# -------------------------------------------------
controller = AgentController()

# -------------------------------------------------
# Input
# -------------------------------------------------
question = st.text_area(
    "💬 Ask a question",
    placeholder="e.g. Alice has 3 red apples and twice as many green apples. How many apples total?",
    height=120
)

# -------------------------------------------------
# Run button
# -------------------------------------------------
if st.button("🚀 Run Agent", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            start_time = time.time()
            result = controller.solve(question)
            elapsed = round(time.time() - start_time, 2)

        st.divider()

        # -------------------------------------------------
        # Result handling
        # -------------------------------------------------
        if result["status"] == "success":
            st.success("✅ Final Answer")
            st.markdown(f"### {result['answer']}")

            # ---- Provider badge (if available) ----
            metadata = result.get("metadata", {})
            provider = metadata.get("provider")
            latency = metadata.get("latency")

            cols = st.columns(3)
            cols[0].metric("⏱️ Time", f"{elapsed}s")

            if provider:
                cols[1].metric("🤖 Provider", provider)

            if latency:
                cols[2].metric("⚡ LLM Latency", f"{latency}s")

            # ---- Reasoning ----
            with st.expander("🧠 High-Level Reasoning (User-Safe)"):
                reasoning = result.get("reasoning")
                if isinstance(reasoning, dict):
                    st.json(reasoning)
                else:
                    st.write(reasoning)

        else:
            st.error("❌ Agent failed to produce a reliable answer.")
            st.write(result.get("error", "Unknown error"))

            with st.expander("🔍 Debug & Transparency"):
                st.json(result)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.divider()
st.caption(
    "Built with deterministic logic + LLM reasoning · "
    "Designed for reliability and cost efficiency"
)
