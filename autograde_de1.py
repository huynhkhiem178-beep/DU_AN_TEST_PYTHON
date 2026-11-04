"""Cham diem tung y nho cua de Python."""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path
from test_de1 import tests
ROOT = Path(__file__).resolve().parent
DEFAULT_SUBMISSIONS = ROOT / "submissions_de1"
WEIGHTS = {"Cau1a":2/3,"Cau1b":2/3,"Cau1c":2/3,"Cau2a":2/3,"Cau2b":2/3,"Cau2c":2/3,"Cau3a":2/3,"Cau3b":2/3,"Cau3c":2/3,"Cau4a":1.0,"Cau4b":1.0,"Cau5a":1.0,"Cau5b":1.0}
def normalize(s): return " ".join(s.casefold().split())
def run_code(path, data, timeout=5.0):
    try:
        import os
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUTF8"] = "1"
        r = subprocess.run([sys.executable, str(path)], input=data, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=timeout, cwd=path.parent, env=env)
        return [x.strip() for x in r.stdout.splitlines() if x.strip()], (r.stderr.strip() if r.returncode else None)
    except subprocess.TimeoutExpired: return [], "Qua thoi gian cho (timeout)"
def grade(student_id="Chua nhap", base_dir=DEFAULT_SUBMISSIONS):
    total=0.0
    print("\n"+"="*64); print(f"CHAM BAI PYTHON | SINH VIEN: {student_id}"); print("="*64)
    for q, cases in tests.items():
        path=base_dir/f"{q}.py"; weight=WEIGHTS[q]; print(f"\n{q.upper()} ({weight:.2f} diem)")
        if not path.is_file(): print(f"  [FAIL] Khong tim thay {path.name}"); continue
        passed=0
        for i, case in enumerate(cases,1):
            out,err=run_code(path,case["input"]); actual=normalize("\n".join(out))
            ok=err is None and all(normalize(x) in actual for x in case["expected"])
            if ok: passed+=1; print(f"  [PASS] Test {i}")
            else:
                print(f"  [FAIL] Test {i}")
                if err: print("         Loi:",err)
                print("         Can tim:",case["expected"]); print("         Dau ra:",out)
        score=weight*passed/len(cases) if cases else 0.0; total+=score
        print(f"  DIEM: {score:.2f}/{weight:.2f} ({passed}/{len(cases)} test)")
    print("\n"+"="*64); print(f"TONG DIEM: {total:.2f}/10"); print("="*64); return total
def main():
    p=argparse.ArgumentParser(); p.add_argument("--student-id",default="Chua nhap"); p.add_argument("--submissions",type=Path,default=DEFAULT_SUBMISSIONS); a=p.parse_args(); grade(a.student_id,a.submissions.resolve())
if __name__=="__main__": main()
