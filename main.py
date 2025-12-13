import json

from agent.planner import Planner
from agent.executor import Executor
from agent.verifier import Verifier
from agent.controller import AgentController


# --- Helper to load prompt files ---
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def initialize_agent():
    # Load prompts
    planner_prompt = load_prompt("prompts/planner_prompt.txt")
    executor_prompt = load_prompt("prompts/executor_prompt.txt")
    verifier_prompt = load_prompt("prompts/verifier_prompt.txt")

    # Initialize modules
    planner = Planner(planner_prompt)
    executor = Executor(executor_prompt)
    verifier = Verifier(verifier_prompt)

    # Create controller
    controller = AgentController(
        planner=planner,
        executor=executor,
        verifier=verifier,
        max_retries=2
    )

    return controller


# Global controller instance
controller = initialize_agent()


def solve(question: str):
    """Public solve function used by CLI, Streamlit, and tests."""
    return controller.solve(question)


# --- CLI Runner ---
if __name__ == "__main__":
    print("Multi-Step Reasoning Agent")
    print("Type a question below. Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("Question: ").strip()
        except EOFError:
            break

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        if not user_input:
            print("Please enter a question.\n")
            continue

        # Run the agent
        result = solve(user_input)

        print("\n--- RESULT --------------------------------")
        print(json.dumps(result, indent=2))
        print("-------------------------------------------\n")
