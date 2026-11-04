"""Cham tu dong 5 file bai lam theo de thi Python 11301."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from test_de1 import tests

ROOT = Path(__file__).resolve().parent
SUBMISSIONS = ROOT / "submissions_de1"


def normalize(value: str) -> str:
    return " ".join(value.casefold().split())


def run_code(file_path: Path, input_data: str, timeout: float = 5.0) -> tuple[list[str], str | None]:
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=timeout,
            cwd=ROOT,
        )
        output = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        error = result.stderr.strip() if result.returncode != 0 else None
        return output, error
    except subprocess.TimeoutExpired:
        return [], "Qua thoi gian cho (timeout)"


def grade(student_id: str = "Chua nhap", base_dir: Path = SUBMISSIONS) -> float:
    total = 0.0
    print("\n" + "=" * 62)
    print(f"CHAM BAI DE 11301 | SINH VIEN: {student_id}")
    print("=" * 62)

    for question, cases in tests.items():
        file_path = base_dir / f"{question}.py"
        print(f"\n{question.upper()}")

        if not file_path.is_file():
            print(f"  [FAIL] Khong tim thay file: {file_path}")
            print("  DIEM: 0.00/2")
            continue

        passed_count = 0
        for index, case in enumerate(cases, 1):
            output, error = run_code(file_path, case["input"])
            combined = normalize("\n".join(output))
            expected_items = case["expected"]
            passed = error is None and all(normalize(item) in combined for item in expected_items)
            if passed:
                passed_count += 1
                print(f"  [PASS] Test {index}")
            else:
                print(f"  [FAIL] Test {index}")
                if error:
                    print(f"         Loi: {error}")
                print(f"         Can tim: {expected_items}")
                print(f"         Dau ra: {output}")

        score = 2 * passed_count / len(cases) if cases else 0.0
        total += score
        print(f"  KET QUA {question}: {passed_count}/{len(cases)} test | DIEM: {score:.2f}/2")

    print("\n" + "=" * 62)
    print(f"TONG DIEM: {total:.2f}/10")
    print("=" * 62)
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Cham bai thuc hanh Python de 11301")
    parser.add_argument("--student-id", default="Chua nhap")
    parser.add_argument("--submissions", type=Path, default=SUBMISSIONS)
    args = parser.parse_args()
    grade(args.student_id, args.submissions)


if __name__ == "__main__":
    main()
