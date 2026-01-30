from matcher import gale_shapely, get_input
from verifier import verifier
import time

MATCHER_OUTPUT_FILEPATH = "../data/matcher_benchmark_results.out"
VERIFIER_OUTPUT_FILEPATH = "../data/verifier_benchmark_results.out"

input_files = [
    "../tests/test_n_1.in",
    "../tests/test_n_2.in",
    "../tests/test_n_4.in",
    "../tests/test_n_8.in",
    "../tests/test_n_16.in",
    "../tests/test_n_32.in",
    "../tests/test_n_64.in",
    "../tests/test_n_128.in",
    "../tests/test_n_256.in",
    "../tests/test_n_512.in",
]

def benchmark():
    matcher_results = []
    verifier_results= []

    for input_file in input_files:
        n, hospital_prefs, student_prefs = get_input(input_file)

        # Benchmark matcher
        start_time = time.time()
        matches = gale_shapely(n, hospital_prefs, student_prefs)
        end_time = time.time()

        matcher_time = end_time - start_time

        matcher_results.append((n, matcher_time))

        # Benchmark verifier
        start_time = time.time()
        is_valid = verifier((n, hospital_prefs, student_prefs), matches)
        end_time = time.time()

        verifier_time = end_time - start_time

        verifier_results.append((n, verifier_time))

    # Write results to output files
    with open(MATCHER_OUTPUT_FILEPATH, "w") as f:
        for n, elapsed_time in matcher_results:
            f.write(f"{n},{elapsed_time:.6f}\n")

    with open(VERIFIER_OUTPUT_FILEPATH, "w") as f:
        for n, elapsed_time in verifier_results:
            f.write(f"{n},{elapsed_time:.6f}\n")

if __name__ == "__main__":
    benchmark()

