import pytest
from src.exam_tasks import read_list_until_zero, sum_positive_even, count_occurrences

def test_read_list_stops_before_zero():
    assert read_list_until_zero([2, -3, 4, 0, 8]) == [2, -3, 4]

def test_read_list_without_zero_keeps_all_values():
    assert read_list_until_zero([1, 2, 3]) == [1, 2, 3]

def test_read_list_zero_first_returns_empty():
    assert read_list_until_zero([0, 5]) == []

def test_read_list_rejects_non_integer():
    with pytest.raises(TypeError):
        read_list_until_zero([1, "2", 3])

def test_sum_positive_even_only():
    assert sum_positive_even([2, -4, 5, 8, 0, -6]) == 10

def test_sum_positive_even_empty_or_no_match():
    assert sum_positive_even([]) == 0
    assert sum_positive_even([-2, 1, 3]) == 0

def test_count_occurrences_existing_and_missing():
    numbers = [1, 2, 2, 3, 2]
    assert count_occurrences(numbers, 2) == 3
    assert count_occurrences(numbers, 9) == 0

def test_count_occurrences_empty_list():
    assert count_occurrences([], 1) == 0
