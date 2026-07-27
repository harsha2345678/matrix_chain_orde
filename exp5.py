import random

# ----------------------------------------
# Global Comparison Counter
# ----------------------------------------
comparison_count = 0


# ----------------------------------------
# Divide and Conquer Algorithm
# ----------------------------------------
def min_max_dc(arr, low, high):
    """
    Find Minimum and Maximum using Divide and Conquer.
    """

    global comparison_count

    # Base Case: Only one element
    if low == high:
        return arr[low], arr[low]

    # Base Case: Two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    # Conquer
    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine Results
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# ----------------------------------------
# Naive Method
# ----------------------------------------
def min_max_naive(arr):
    """
    Find Minimum and Maximum using the naive approach.
    """

    minimum = arr[0]
    maximum = arr[0]

    comparisons = 0

    for value in arr[1:]:

        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


# ----------------------------------------
# Main Program
# ----------------------------------------
def main():

    global comparison_count

    # Sample Array
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    comparison_count = 0

    minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
    dc_comparisons = comparison_count

    _, _, naive_comparisons = min_max_naive(arr)

    # Display Results
    print("Original Array")
    print(arr)

    print("\nMinimum Element :", minimum)
    print("Maximum Element :", maximum)

    print("\nComparison Analysis")
    print("----------------------------")
    print(f"Divide & Conquer : {dc_comparisons}")
    print(f"Naive Method     : {naive_comparisons}")

    # Performance Analysis
    print("\nPerformance Analysis")
    print("-" * 60)
    print(f"{'Array Size':<12}{'D&C':<12}{'Naive':<12}{'Formula (3n/2 - 2)'}")
    print("-" * 60)

    for size in [10, 100, 1000, 10000]:

        arr = [random.randint(1, 10000) for _ in range(size)]

        comparison_count = 0

        min_max_dc(arr, 0, len(arr) - 1)
        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = (3 * size) // 2 - 2

        print(f"{size:<12}{dc:<12}{naive:<12}{formula}")


# ----------------------------------------
# Driver Code
# ----------------------------------------
if __name__ == "__main__":
    main()