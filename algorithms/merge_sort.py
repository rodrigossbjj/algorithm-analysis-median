from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def median_merge_sort(a: List[int], b: List[int]) -> float:
    """Junta os dois vetores e ordena o resultado (O(n log n))."""
    combined = a + b
    combined = merge_sort(combined)
    n = len(combined)
    mid = n // 2
    if n % 2 == 1:
        return float(combined[mid])
    return (combined[mid - 1] + combined[mid]) / 2.0
