@echo off
title BPSC TRE 4.0 - Sync Folder to Phone
color 0b
echo ============================================================
echo   BPSC TRE 4.0 - 1-Click Sync to Phone
echo ============================================================
echo.
echo Syncing this folder (your master database) to your phone...
echo.

git add .
git commit -m "Update daily study packs and questions"
git push origin master

echo.
echo ============================================================
echo   SYNC SUCCESSFUL!
echo.
echo   Your phone is updated with all current files in this folder.
echo   Open on your phone:
echo   https://nadeemalam178.github.io/bpsc-tre4-prep/
echo ============================================================
echo.
pause
