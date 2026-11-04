@echo off
chcp 65001 > nul
cd /d "%~dp0"
title CHAM DIEM BAI LAM PYTHON

echo ================================================
echo          CHUONG TRINH CHAM DIEM PYTHON
echo ================================================
echo.

py -m autograder.grade "submissions/de1/bai_lam.py" --student-id SV001

echo.
pause
