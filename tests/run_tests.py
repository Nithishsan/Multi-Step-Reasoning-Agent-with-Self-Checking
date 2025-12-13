import pytest

print("🚀 Running All Test Suites...\n")

pytest.main(["-q", "tests/test_easy_cases.py"])
pytest.main(["-q", "tests/test_tricky_cases.py"])

print("\n✅ All tests completed.")
