@echo off
setlocal
cd /d %~dp0
python -W ignore uilauncher.py
pause
