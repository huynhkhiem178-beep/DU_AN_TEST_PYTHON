"""Smoke test dap an mau cho ca 13 y nho."""
from pathlib import Path
from autograde_de1 import run_code
ROOT=Path(__file__).resolve().parents[1]
ANSWERS=ROOT/"submissions_de1_dapan"
CASES={
    "Cau1a": "635\n",
    "Cau1b": "635\n",
    "Cau1c": "1\n",
    "Cau2a": "AbCxyz\n",
    "Cau2b": "madam\n",
    "Cau2c": "a1b2c3\n",
    "Cau3a": "2\n-3\n4\n0\n",
    "Cau3b": "2\n-3\n4\n0\n",
    "Cau3c": "2\n3\n2\n0\n2\n",
    "Cau4a": "1\nS01\nDe Men Phieu Luu Ky\nTo Hoai\nKim Dong\n1941\n",
    "Cau4b": "1\nS01\nSach mau\nTac gia\nNXB Tre\n2020\nS01\n",
    "Cau5a": "",
    "Cau5b": ""
}
def test_all_reference_answers_run():
    for name,data in CASES.items():
        output,error=run_code(ANSWERS/f"{name}.py",data)
        assert error is None, f"{name}: {error}"
        assert output, f"{name}: khong co dau ra"
