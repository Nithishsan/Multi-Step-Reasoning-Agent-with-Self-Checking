import time
import concurrent.futures
from main import solve

TEST_QUESTIONS = [
    "What is 10 + 4?",
    "How long is a trip from 11:15 to 14:50?",
    "If Bob has 5 apples and Carol has twice Bob's apples, total?",
] * 5  # total 15 parallel queries


def run_parallel_test():
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(solve, TEST_QUESTIONS))

    end = time.time()

    print(f"⏱ Total time for 15 requests: {round(end - start, 2)} sec")
    print(f"Avg time per request: {round((end - start) / len(TEST_QUESTIONS), 2)} sec\n")

    for r in results[:3]:
        print("Sample Output:", r["answer"])


if __name__ == "__main__":
    print("🔥 Throughput / Parallel Performance Test\n")
    run_parallel_test()
