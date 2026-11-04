import pytest
from src.exam_tasks import count_uppercase, is_palindrome, sum_digits_in_text

@pytest.mark.parametrize("text, expected", [("Hello WORLD", 6), ("python", 0), ("ABC123", 3), ("", 0)])
def test_count_uppercase(text, expected):
    assert count_uppercase(text) == expected

@pytest.mark.parametrize("text, expected", [("madam", True), ("abba", True), ("python", False), ("", True), ("Abba", False)])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected

@pytest.mark.parametrize("text, expected", [("abc123", 6), ("A1B2C3", 6), ("khong co so", 0), ("", 0), ("9-8-7", 24)])
def test_sum_digits_in_text(text, expected):
    assert sum_digits_in_text(text) == expected

def test_string_functions_reject_non_string():
    with pytest.raises(TypeError): count_uppercase(123)
    with pytest.raises(TypeError): is_palindrome(None)
    with pytest.raises(TypeError): sum_digits_in_text(123)
