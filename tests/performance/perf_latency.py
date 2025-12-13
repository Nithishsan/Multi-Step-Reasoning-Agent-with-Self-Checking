import time
from main import solve

QUESTIONS = [
    "What is 15 + 27?",
    "A train leaves at 09:15 and arrives at 13:55. How long is the journey?",
    "Alice has 3 apples and gets twice as many from Bob. Total?",
]

def measure_latency():
    results = []

    for q in QUESTIONS:
        start = time.time()
        output = solve(q)
        end = time.time()

        results.append({
            "question": q,
            "status": output["status"],
            "time_sec": round(end - start, 3),
            "retries": output["metadata"]["retries"]
        })

    return results


if __name__ == "__main__":
    print("⚡ Latency Performance Test\n")
    results = measure_latency()

    for r in results:
        print(
            f"Q: {r['question']}\n"
            f"Time: {r['time_sec']} sec | Retries: {r['retries']}\n"
        )
