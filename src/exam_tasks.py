"""Các hàm theo đề thi Lập trình Python mã 11301."""
from dataclasses import dataclass
from datetime import date

def validate_n(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n phải là số nguyên")
    if not 1 <= n <= 1500:
        raise ValueError("n phải nằm trong đoạn [1, 1500]")
    return n

def count_odd_digits(n: int) -> int:
    validate_n(n)
    return sum(int(ch) % 2 == 1 for ch in str(n))

def sum_reciprocal_even(n: int) -> float:
    """Tính S = 1/2 + 1/4 + ... + 1/(2*n), theo đáp án đề thi."""
    validate_n(n)
    return sum(1 / (2 * i) for i in range(1, n + 1))

def count_uppercase(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text phải là chuỗi")
    return sum(ch.isupper() for ch in text)

def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text phải là chuỗi")
    return text == text[::-1]

def sum_digits_in_text(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text phải là chuỗi")
    return sum(int(ch) for ch in text if ch.isdigit())

def read_list_until_zero(values: list[int]) -> list[int]:
    """Số 0 là dấu kết thúc và không được lưu vào danh sách."""
    result = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Mỗi phần tử phải là số nguyên")
        if value == 0:
            break
        result.append(value)
    return result

def sum_positive_even(numbers: list[int]) -> int:
    return sum(n for n in numbers if n > 0 and n % 2 == 0)

def count_occurrences(numbers: list[int], k: int) -> int:
    return numbers.count(k)

def add_book(books: dict, ma_so: str, ten_sach: str, ten_tac_gia: str,
             nha_xuat_ban: str, nam_xuat_ban: int) -> dict:
    """Thêm/cập nhật sách; mã số sách là khóa của từ điển."""
    if not ma_so:
        raise ValueError("Mã số sách không được để trống")
    if isinstance(nam_xuat_ban, bool) or not isinstance(nam_xuat_ban, int):
        raise TypeError("Năm xuất bản phải là số nguyên")
    if not 1 <= nam_xuat_ban <= date.today().year:
        raise ValueError(f"Năm xuất bản phải từ 1 đến {date.today().year}")
    books[ma_so] = {
        "ten_sach": ten_sach,
        "ten_tac_gia": ten_tac_gia,
        "nha_xuat_ban": nha_xuat_ban,
        "nam_xuat_ban": nam_xuat_ban,
    }
    return books

def delete_book(books: dict, ma_so: str) -> bool:
    if ma_so not in books:
        return False
    del books[ma_so]
    return True

@dataclass
class DienThoai:
    MaMay: str
    TenMay: str
    HangSanXuat: str
    DungLuongPin: int
    GiaBan: int

    def thongtindienthoai(self) -> str:
        return (
            f"Ma may: {self.MaMay}\n"
            f"Ten may: {self.TenMay}\n"
            f"Hang san xuat: {self.HangSanXuat}\n"
            f"Dung luong pin: {self.DungLuongPin}\n"
            f"Gia ban: {self.GiaBan}"
        )
