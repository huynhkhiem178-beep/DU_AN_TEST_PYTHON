import pytest

from autograder.grade import run_case
from src import exam_tasks


def test_run_case_accepts_correct_function_result():
    case = {
        "function": "count_odd_digits",
        "args": [635],
        "expected": 2,
    }
    passed, message = run_case(exam_tasks, case)
    assert passed is True
    assert message == "Đúng"


def test_run_case_detects_wrong_result():
    case = {
        "function": "count_odd_digits",
        "args": [635],
        "expected": 3,
    }
    passed, message = run_case(exam_tasks, case)
    assert passed is False
    assert "mong đợi" in message


def test_run_case_checks_expected_exception():
    case = {
        "function": "validate_n",
        "args": [0],
        "expected_error": "ValueError",
    }
    passed, message = run_case(exam_tasks, case)
    assert passed is True
    assert "ValueError" in message


def test_run_case_reports_missing_function():
    case = {"function": "function_not_found", "args": [], "expected": None}
    passed, message = run_case(exam_tasks, case)
    assert passed is False
    assert "Thiếu hàm/lớp" in message


def test_run_case_checks_dataclass_attributes():
    case = {
        "function": "DienThoai",
        "args": ["DT01", "iPhone", "Apple", 3000, 1000],
        "expected": {
            "MaMay": "DT01",
            "TenMay": "iPhone",
            "HangSanXuat": "Apple",
            "DungLuongPin": 3000,
            "GiaBan": 1000,
        },
    }
    passed, message = run_case(exam_tasks, case)
    assert passed is True
    assert message == "Đúng"
