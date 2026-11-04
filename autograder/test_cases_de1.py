"""Bộ dữ liệu kiểm thử cho đề 11301.

Mỗi câu có tối đa 2 điểm. Các test case được chia đều điểm trong câu.
Đây là bộ test dựa trên mô tả đề đã dùng để xây dựng src/exam_tasks.py.
"""
from datetime import date

TESTS = {
    "Cau1": [
        {"function": "validate_n", "args": [1], "expected": 1},
        {"function": "validate_n", "args": [1500], "expected": 1500},
        {"function": "validate_n", "args": [0], "expected_error": "ValueError"},
        {"function": "count_odd_digits", "args": [635], "expected": 2},
        {"function": "count_odd_digits", "args": [468], "expected": 0},
        {"function": "sum_reciprocal_even", "args": [1], "expected": 0.5},
        {"function": "sum_reciprocal_even", "args": [2], "expected": 0.75},
    ],
    "Cau2": [
        {"function": "count_uppercase", "args": ["Hello WORLD"], "expected": 6},
        {"function": "count_uppercase", "args": ["python"], "expected": 0},
        {"function": "is_palindrome", "args": ["madam"], "expected": True},
        {"function": "is_palindrome", "args": ["Python"], "expected": False},
        {"function": "sum_digits_in_text", "args": ["abc123"], "expected": 6},
        {"function": "sum_digits_in_text", "args": ["A1B2C3"], "expected": 6},
    ],
    "Cau3": [
        {"function": "read_list_until_zero", "args": [[2, -3, 4, 0, 8]], "expected": [2, -3, 4]},
        {"function": "read_list_until_zero", "args": [[0, 5]], "expected": []},
        {"function": "sum_positive_even", "args": [[2, -4, 5, 8, 0, -6]], "expected": 10},
        {"function": "sum_positive_even", "args": [[-2, 1, 3]], "expected": 0},
        {"function": "count_occurrences", "args": [[1, 2, 2, 3, 2], 2], "expected": 3},
        {"function": "count_occurrences", "args": [[1, 2, 3], 9], "expected": 0},
    ],
    "Cau4": [
        {
            "function": "add_book",
            "args": [{}, "S01", "De Men Phieu Luu Ky", "To Hoai", "Kim Dong", 1941],
            "expected": {
                "S01": {
                    "ten_sach": "De Men Phieu Luu Ky",
                    "ten_tac_gia": "To Hoai",
                    "nha_xuat_ban": "Kim Dong",
                    "nam_xuat_ban": 1941,
                }
            },
        },
        {
            "function": "delete_book",
            "args": [{"S01": {"ten_sach": "Python"}}, "S01"],
            "expected": True,
        },
        {
            "function": "delete_book",
            "args": [{"S01": {"ten_sach": "Python"}}, "S99"],
            "expected": False,
        },
        {
            "function": "add_book",
            "args": [{}, "S02", "Sach", "Tac gia", "NXB", date.today().year + 1],
            "expected_error": "ValueError",
        },
    ],
    "Cau5": [
        {
            "function": "DienThoai",
            "args": ["DT01", "iPhone 15 Pro", "Apple", 3274, 28990000],
            "expected": {
                "MaMay": "DT01",
                "TenMay": "iPhone 15 Pro",
                "HangSanXuat": "Apple",
                "DungLuongPin": 3274,
                "GiaBan": 28990000,
            },
        },
        {
            "function": "DienThoai",
            "args": ["DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000],
            "expected": {
                "MaMay": "DT02",
                "TenMay": "Galaxy S24 Ultra",
                "HangSanXuat": "Samsung",
                "DungLuongPin": 5000,
                "GiaBan": 29990000,
            },
        },
    ],
}
