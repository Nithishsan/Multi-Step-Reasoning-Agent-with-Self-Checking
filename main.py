from agent.controller import AgentController

controller = AgentController()

print("\n🧠 Multi-Step Reasoning Agent\n")

while True:
    q = input("Enter question (or exit): ").strip()
    if q.lower() == "exit":
        break

    result = controller.solve(q)
    print("\nResult:\n", result)
