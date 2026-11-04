"""Pytest smoke tests cho cac file dap an cua de 11301."""
from pathlib import Path
from autograde_de1 import run_code

ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS = ROOT / "submissions_de1_dapan"

def test_cau1a_runs():
    output, error = run_code(SUBMISSIONS / "Cau1a.py", "635\n")
    assert error is None
    assert any("635" in line for line in output)

def test_cau1b_runs():
    output, error = run_code(SUBMISSIONS / "Cau1b.py", "635\n")
    assert error is None
    assert any("2" in line for line in output)

def test_cau1c_runs():
    output, error = run_code(SUBMISSIONS / "Cau1c.py", "2\n")
    assert error is None
    assert any("0.75" in line for line in output)

def test_cau2_runs():
    output, error = run_code(SUBMISSIONS / "Cau2.py", "madam\n")
    assert error is None
    assert any("True" in line for line in output)

def test_cau3_runs():
    output, error = run_code(SUBMISSIONS / "Cau3.py", "2\n0\n2\n")
    assert error is None
    assert any("[2]" in line for line in output)

def test_cau4_runs():
    data = "1\nS01\nSach\nTac gia\nNXB\n2020\nS01\n"
    output, error = run_code(SUBMISSIONS / "Cau4.py", data)
    assert error is None
    assert any("Da xoa sach" in line for line in output)

def test_cau5_runs():
    output, error = run_code(SUBMISSIONS / "Cau5.py", "")
    assert error is None
    assert any("iPhone 15 Pro" in line for line in output)
