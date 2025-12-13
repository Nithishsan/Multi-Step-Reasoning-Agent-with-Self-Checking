import time
from main import solve

BASE_QUESTION = (
    "Alice has 3 red apples and twice as many green apples. "
    "How many apples does she have?"
)

def generate_long_question(multiplier: int):
    filler = " This is additional irrelevant context." * multiplier
    return BASE_QUESTION + filler


def run_scale_test():
    for length in [0, 10, 50, 100, 200]:
        question = generate_long_question(length)
        
        start = time.time()
        output = solve(question)
        end = time.time()
        
        print(
            f"Scale x{length}: "
            f"{round(end - start, 3)} sec "
            f"| Retries: {output['metadata']['retries']} "
            f"| Status: {output['status']}"
        )


if __name__ == "__main__":
    print("📏 Scaling Performance Test\n")
    run_scale_test()
