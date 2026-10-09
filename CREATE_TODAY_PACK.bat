@echo off
title BPSC TRE 4.0 - Auto Create Today Study Pack
color 0b
echo ============================================================
echo   BPSC TRE 4.0 - 1-Click Daily Study Pack Generator
echo ============================================================
echo.
echo Scanning previous days and auto-generating next study module...
echo.

python "%~dp0new_day.py"

echo.
echo Done! You can now open index.html or start the mobile server.
echo.
pause
