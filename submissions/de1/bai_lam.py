"""File để tự viết lời giải và thử chấm điểm đề 01.

Bạn có thể viết thuật toán theo cách riêng, nhưng cần giữ đúng tên hàm,
tham số và kiểu kết quả mà bộ chấm yêu cầu. Xem src/exam_tasks.py.
"""

from dataclasses import dataclass


def validate_n(n: int) -> int:
    # TODO: Kiểm tra n thuộc [1, 1500], hợp lệ thì trả về n.
    raise NotImplementedError


def count_odd_digits(n: int) -> int:
    # TODO: Đếm chữ số lẻ của n.
    raise NotImplementedError


def sum_reciprocal_even(n: int) -> float:
    # TODO: Tính 1/2 + 1/4 + ... + 1/(2*n).
    raise NotImplementedError


def count_uppercase(text: str) -> int:
    # TODO: Đếm số ký tự in hoa.
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    # TODO: Kiểm tra chuỗi đối xứng.
    raise NotImplementedError


def sum_digits_in_text(text: str) -> int:
    # TODO: Tính tổng các chữ số xuất hiện trong chuỗi.
    raise NotImplementedError


def read_list_until_zero(values: list[int]) -> list[int]:
    # TODO: Lấy các phần tử trước số 0; không lấy số 0.
    raise NotImplementedError


def sum_positive_even(numbers: list[int]) -> int:
    # TODO: Tính tổng các số dương chẵn.
    raise NotImplementedError


def count_occurrences(numbers: list[int], k: int) -> int:
    # TODO: Đếm số lần k xuất hiện trong danh sách.
    raise NotImplementedError


def add_book(
    books: dict,
    ma_so: str,
    ten_sach: str,
    ten_tac_gia: str,
    nha_xuat_ban: str,
    nam_xuat_ban: int,
) -> dict:
    # TODO: Thêm sách vào từ điển theo đúng cấu trúc expected trong test_cases_de1.py.
    raise NotImplementedError


def delete_book(books: dict, ma_so: str) -> bool:
    # TODO: Xóa sách theo mã; trả về True nếu xóa được, False nếu không có.
    raise NotImplementedError


@dataclass
class DienThoai:
    MaMay: str
    TenMay: str
    HangSanXuat: str
    DungLuongPin: int
    GiaBan: int

    def thongtindienthoai(self) -> str:
        # TODO: Trả về thông tin điện thoại theo định dạng yêu cầu của đề.
        raise NotImplementedError
