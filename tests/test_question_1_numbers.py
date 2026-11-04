import pytest
from src.exam_tasks import validate_n, count_odd_digits, sum_reciprocal_even

@pytest.mark.parametrize("n", [1, 635, 1500])
def test_validate_n_accepts_range(n):
    assert validate_n(n) == n

@pytest.mark.parametrize("n", [0, -1, 1501, 9999])
def test_validate_n_rejects_out_of_range(n):
    with pytest.raises(ValueError):
        validate_n(n)

def test_validate_n_rejects_non_integer():
    with pytest.raises(TypeError):
        validate_n(3.5)

@pytest.mark.parametrize("n, expected", [(635, 2), (1, 1), (468, 0), (1500, 2)])
def test_count_odd_digits(n, expected):
    assert count_odd_digits(n) == expected

def test_count_odd_digits_rejects_out_of_range():
    with pytest.raises(ValueError):
        count_odd_digits(13579)

def test_sum_reciprocal_even_n_1():
    assert sum_reciprocal_even(1) == pytest.approx(0.5)

def test_sum_reciprocal_even_n_2():
    assert sum_reciprocal_even(2) == pytest.approx(0.75)

def test_sum_reciprocal_even_rejects_invalid_n():
    with pytest.raises(ValueError):
        sum_reciprocal_even(1501)
