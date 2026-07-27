import time
import random


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm

    Time Complexity:
        Best/Average : O(log log n)
        Worst        : O(n)

    Space Complexity: O(1)
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Avoid division by zero
        if arr[high] == arr[low]:
            break

        # Interpolation Formula
        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    """Compare Interpolation Search and Binary Search."""

    sizes = [1000, 5000, 10000, 50000, 100000]

    print(
        f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
        f"{'IS Comparisons':>16} {'BS Comparisons':>16}"
    )
    print("-" * 75)

    for size in sizes:

        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        # Interpolation Search Timing
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search Timing
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(
            f"{size:>10} "
            f"{is_time:>14.4f} "
            f"{bs_time:>14.4f} "
            f"{comp_is:>16} "
            f"{comp_bs:>16}"
        )


# ---------------- Main Program ---------------- #

arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

index, comparisons = interpolation_search(arr, target)

print("Array:", arr)
print("Searching for:", target)
print(f"Found at index: {index}")
print(f"Comparisons: {comparisons}")

print("\nPerformance Analysis:\n")
performance_analysis()