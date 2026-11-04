@echo off
chcp 65001 > nul
cd /d "%~dp0"
py autograde_de1.py --student-id SV001
pause
