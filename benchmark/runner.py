import time
import statistics
from typing import List

from algorithms import median_merge_sort, median_divide_and_conquer
from .data_gen import generate_sorted_pair


def benchmark(sizes: List[int], repeats: int = 5) -> dict:
    results = {
        "sizes": sizes,
        "algo1_times": [],
        "algo2_times": [],
    }

    for size in sizes:
        t1_samples, t2_samples = [], []

        for _ in range(repeats):
            a, b = generate_sorted_pair(size)

            start = time.perf_counter()
            r1 = median_merge_sort(a, b)
            t1_samples.append(time.perf_counter() - start)

            start = time.perf_counter()
            r2 = median_divide_and_conquer(a, b)
            t2_samples.append(time.perf_counter() - start)

            assert abs(r1 - r2) < 1e-9, f"Divergência: {r1} != {r2}"

        results["algo1_times"].append(statistics.mean(t1_samples))
        results["algo2_times"].append(statistics.mean(t2_samples))

        print(
            f"n={size:>8,}  |  Algo1: {results['algo1_times'][-1]*1000:8.3f} ms  |  Algo2: {results['algo2_times'][-1]*1000:8.6f} ms"
        )

    return results


if __name__ == "__main__":
    SIZES = [1_000, 5_000, 10_000, 30_000, 50_000, 75_000, 100_000]
    REPEATS = 5
    benchmark(SIZES, REPEATS)
