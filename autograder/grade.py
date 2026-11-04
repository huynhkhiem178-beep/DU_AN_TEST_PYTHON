"""Chương trình chấm tự động một file bài làm Python."""
from __future__ import annotations

import argparse
import importlib.util
import math
from dataclasses import asdict, is_dataclass
from pathlib import Path
from types import ModuleType
from typing import Any

from autograder.test_cases_de1 import TESTS


def load_submission(file_path: str | Path) -> ModuleType:
    """Nạp file bài làm để có thể gọi các hàm trong đó."""
    path = Path(file_path).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file bài làm: {path}")

    spec = importlib.util.spec_from_file_location("student_submission", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Không thể đọc file bài làm: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def values_equal(actual: Any, expected: Any) -> bool:
    """So sánh kết quả, có hỗ trợ sai số nhỏ đối với số thực."""
    if isinstance(actual, (int, float)) and not isinstance(actual, bool):
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            return math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
    return actual == expected


def run_case(module: ModuleType, case: dict[str, Any]) -> tuple[bool, str]:
    """Chạy một test case; trả về trạng thái và thông báo."""
    function_name = case["function"]
    target = getattr(module, function_name, None)
    if target is None:
        return False, f"Thiếu hàm/lớp {function_name}"

    try:
        result = target(*case.get("args", []))
        if function_name == "DienThoai":
            if is_dataclass(result):
                result = asdict(result)
            else:
                result = vars(result)

        if "expected_error" in case:
            return False, f"Không phát sinh lỗi {case['expected_error']} như mong đợi"

        expected = case["expected"]
        if values_equal(result, expected):
            return True, "Đúng"
        return False, f"Sai: nhận được {result!r}, mong đợi {expected!r}"

    except Exception as error:  # noqa: BLE001 - hiển thị lỗi bài làm cho sinh viên
        expected_error = case.get("expected_error")
        if expected_error and type(error).__name__ == expected_error:
            return True, f"Đúng (phát sinh {expected_error})"
        return False, f"Lỗi {type(error).__name__}: {error}"


def grade(student_file: str | Path, student_id: str = "Chưa nhập") -> float:
    """Chấm 5 câu, mỗi câu tối đa 2 điểm."""
    module = load_submission(student_file)
    total_score = 0.0

    print(f"\nBẮT ĐẦU CHẤM BÀI: {student_id}")
    print(f"File bài làm: {Path(student_file)}")
    print("=" * 55)

    for question, cases in TESTS.items():
        correct = 0
        print(f"\n{question.upper()}")
        for index, case in enumerate(cases, start=1):
            passed, message = run_case(module, case)
            mark = "PASS" if passed else "FAIL"
            print(f"  [{mark}] Test {index}: {message}")
            correct += int(passed)

        question_score = 2 * correct / len(cases)
        total_score += question_score
        print(f"  Điểm câu: {question_score:.2f}/2 ({correct}/{len(cases)} test)")

    print("\n" + "=" * 55)
    print(f"TỔNG ĐIỂM: {total_score:.2f}/10")
    return total_score


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Chấm tự động bài Python theo đề 11301."
    )
    parser.add_argument(
        "student_file",
        nargs="?",
        default="src/exam_tasks.py",
        help="Đường dẫn đến file .py của sinh viên",
    )
    parser.add_argument("--student-id", default="Chưa nhập", help="Mã sinh viên")
    args = parser.parse_args()
    grade(args.student_file, args.student_id)


if __name__ == "__main__":
    main()
