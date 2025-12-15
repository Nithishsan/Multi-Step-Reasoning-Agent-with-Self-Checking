import streamlit as st
from agent.controller import AgentController

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🧠 Multi-Step Reasoning Agent</h1>
    <p style="text-align:center; color: gray;">
        A hybrid AI system that plans → executes → verifies before answering
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Controller
# --------------------------------------------------
controller = AgentController()

# --------------------------------------------------
# Input Section
# --------------------------------------------------
st.subheader("💬 Ask a Question")

question = st.text_area(
    "Enter your question below:",
    placeholder="e.g. A train leaves at 14:30 and arrives at 18:05. How long is the journey?",
    height=120
)

run = st.button("🚀 Run Agent", use_container_width=True)

# --------------------------------------------------
# Execution
# --------------------------------------------------
if run:
    if not question.strip():
        st.warning("Please enter a question before running the agent.")
    else:
        with st.spinner("🧠 Reasoning in progress..."):
            result = controller.solve(question)

        st.divider()

        # --------------------------------------------------
        # Result Display
        # --------------------------------------------------
        if result["status"] == "success":
            st.success("✅ Final Answer")
            st.markdown(
                f"""
                <div style="font-size: 20px; font-weight: 600;">
                    {result['answer']}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("❌ Agent failed to produce a reliable answer.")
            st.caption(result.get("error", "Unknown error"))

        # --------------------------------------------------
        # Reasoning Summary
        # --------------------------------------------------
        if result.get("reasoning"):
            st.subheader("🧠 High-Level Reasoning (User-Safe)")
            if isinstance(result["reasoning"], str):
                st.write(result["reasoning"])
            else:
                st.json(result["reasoning"])

        # --------------------------------------------------
        # Debug / Transparency Section
        # --------------------------------------------------
        with st.expander("🔍 Debug & Transparency"):
            st.json(result)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()
st.caption(
    "Built with deterministic logic + LLM reasoning · Designed for reliability and cost efficiency"
)
