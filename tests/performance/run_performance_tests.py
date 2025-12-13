import os

print("\n🚀 Running All Performance Tests...\n")

os.system("python tests/performance/perf_latency.py")
os.system("python tests/performance/perf_scale.py")
os.system("python tests/performance/perf_parallel.py")

print("\n✅ Performance Tests Completed.\n")
