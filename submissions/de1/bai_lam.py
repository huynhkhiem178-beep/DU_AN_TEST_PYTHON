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



def _run_autograder() -> None:
    """Cho phép nhấp đúp file này để tự chấm bài trên Windows."""
    import sys
    from pathlib import Path

    submission_path = Path(__file__).resolve()

    # Tìm thư mục gốc dự án để có thể chạy dù mở file từ vị trí khác.
    project_root = next(
        (
            parent
            for parent in submission_path.parents
            if (parent / "autograder" / "grade.py").is_file()
        ),
        None,
    )

    if project_root is None:
        print("KHÔNG TÌM THẤY THƯ MỤC GỐC DỰ ÁN.")
        print("Hãy đặt file này trong DU_AN_TEST_PYTHON/submissions/de1/.")
        input("\nNhấn Enter để thoát...")
        return

    sys.path.insert(0, str(project_root))

    print("=" * 55)
    print("          CHƯƠNG TRÌNH CHẤM ĐIỂM TỰ ĐỘNG")
    print("=" * 55)
    student_id = input("Nhập mã sinh viên (Enter để dùng SV001): ").strip()
    if not student_id:
        student_id = "SV001"

    try:
        from autograder.grade import grade

        grade(submission_path, student_id)
    except Exception as error:
        print(f"\nKhông thể chấm bài: {type(error).__name__}: {error}")

    input("\nNhấn Enter để đóng cửa sổ...")


if __name__ == "__main__":
    _run_autograder()
