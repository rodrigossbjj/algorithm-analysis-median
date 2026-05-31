import pytest

from algorithms import median_merge_sort, median_divide_and_conquer


def test_both_empty():
    with pytest.raises(ValueError):
        median_divide_and_conquer([], [])


def test_small_equal_sizes():
    a = [1, 3, 5]
    b = [2, 4, 6]
    m1 = median_merge_sort(a, b)
    m2 = median_divide_and_conquer(a, b)
    assert m1 == m2 == 3.5


def test_different_sizes():
    a = [1, 2]
    b = [3, 4, 5]
    m1 = median_merge_sort(a, b)
    m2 = median_divide_and_conquer(a, b)
    assert m1 == m2 == 3.0


def test_with_duplicates():
    a = [1, 1, 1]
    b = [1, 1]
    assert median_merge_sort(a, b) == median_divide_and_conquer(a, b)
