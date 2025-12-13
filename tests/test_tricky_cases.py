from main import solve

def test_tricky_cases():
    test_items = [

        # Edge case: midnight crossing
        {
            "question": "A train leaves at 23:10 and arrives at 01:20. How long is the journey?",
            "expected_contains": "2 hours"
        },

        # Multi-step unit mismatch
        {
            "question": "A car travels 60 km in 1 hour. How far does it travel in 150 minutes?",
            "expected_contains": "150"
        },

        # Negative avoidance check
        {
            "question": "If the temperature rises from -3°C to 5°C, what is the change?",
            "expected_contains": "8"
        },

        # Constraint validation
        {
            "question": "A meeting needs 80 minutes. Available slots: 09:00–09:45, 10:00–10:30, 12:00–14:00. Which slots can fit?",
            "expected_contains": "12:00"
        },

        # Relation chain logic
        {
            "question": "Alice has twice as many apples as Bob. Bob has 4 apples. How many do they have together?",
            "expected_contains": "12"
        },
    ]

    for item in test_items:
        result = solve(item["question"])
        assert result["status"] == "success"
        assert item["expected_contains"] in result["answer"]
        print(f"[PASS] {item['question']}")
