import matplotlib.pyplot as plt

iterations = []
times = []

# Plot matcher benchmark results
with open("../data/matcher_benchmark_results.out") as f:
    for line in f:
        n, runtime = line.strip().split(",")
        iterations.append(int(n))
        times.append(float(runtime))

plt.plot(iterations, times, marker="o")
plt.xlabel("n (input size)")
plt.ylabel("Runtime (seconds)")
plt.title("Matcher Runtime vs Input Size")
plt.savefig("../graphs/matcher_runtime_plot.png", dpi=300)
plt.show()
iterations = []
times = []

# Plot verifier benchmark results
with open("../data/verifier_benchmark_results.out") as f:
    for line in f:
        n, runtime = line.strip().split(",")
        iterations.append(int(n))
        times.append(float(runtime))

plt.plot(iterations, times, marker="o")
plt.xlabel("n (input size)")
plt.ylabel("Runtime (seconds)")
plt.title("Verifier Runtime vs Input Size")
plt.savefig("../graphs/verifier_runtime_plot.png", dpi=300)
plt.show()

