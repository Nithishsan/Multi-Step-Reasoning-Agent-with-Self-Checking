from main import solve

def test_easy_cases():
    test_items = [
        {
            "question": "What is 7 + 5?",
            "expected_contains": "12"
        },
        {
            "question": "A train leaves at 14:30 and arrives at 18:05. How long is the journey?",
            "expected_contains": "3 hours"
        },
        {
            "question": "Alice has 3 red apples and twice as many green apples. How many apples does she have?",
            "expected_contains": "9"
        },
        {
            "question": "John walks 2 km in the morning and 3 km in the evening. What is his total distance?",
            "expected_contains": "5"
        },
        {
            "question": "If a bottle costs 20 and you buy 3, how much do you pay?",
            "expected_contains": "60"
        },
        {
            "question": "What is the difference between 50 and 18?",
            "expected_contains": "32"
        },
        {
            "question": "A box contains 4 blue balls and 6 red balls. How many balls are there?",
            "expected_contains": "10"
        },
        {
            "question": "Convert 120 minutes into hours.",
            "expected_contains": "2"
        }
    ]

    for item in test_items:
        result = solve(item["question"])
        assert result["status"] == "success"
        assert item["expected_contains"] in result["answer"]
        print(f"[PASS] {item['question']}")
