import re


def solve_word_problem(question: str):
    """
    Deterministic solver for common word-based arithmetic problems.
    Returns an int if solvable, otherwise None.
    """

    q = question.lower()
    numbers = list(map(int, re.findall(r"\d+", q)))

    # -------------------------------------------------
    # 1️⃣ "twice as many"
    # Alice has 3 apples and twice as many bananas
    # -------------------------------------------------
    if "twice as many" in q and len(numbers) == 1:
        base = numbers[0]
        return base + (2 * base)

    # -------------------------------------------------
    # 2️⃣ "half of"
    # Half of 20 chocolates are eaten
    # -------------------------------------------------
    if "half of" in q and len(numbers) == 1:
        return numbers[0] // 2

    # -------------------------------------------------
    # 3️⃣ gives away / buys more
    # Alice has 10 apples, gives 3, buys 5
    # -------------------------------------------------
    if "gives" in q and "buys" in q and len(numbers) >= 3:
        start, given, bought = numbers[:3]
        return start - given + bought

    # -------------------------------------------------
    # 4️⃣ each / per-item multiplication
    # 3 bags, each has 4 apples
    # -------------------------------------------------
    if ("each" in q or "per" in q) and len(numbers) >= 2:
        return numbers[0] * numbers[1]

    # -------------------------------------------------
    # 5️⃣ total items
    # Total of 5 red balls and 7 blue balls
    # -------------------------------------------------
    if "total" in q and len(numbers) >= 2:
        return sum(numbers)

    # -------------------------------------------------
    # 6️⃣ remaining after removal
    # 20 candies, 6 eaten, how many left
    # -------------------------------------------------
    if ("left" in q or "remaining" in q) and len(numbers) >= 2:
        return numbers[0] - numbers[1]

    # -------------------------------------------------
    # 7️⃣ combined groups
    # 3 boys and 4 girls
    # -------------------------------------------------
    if ("and" in q) and len(numbers) == 2:
        return numbers[0] + numbers[1]

    return None
