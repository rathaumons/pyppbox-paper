@echo off
setlocal
cd /d %~dp0
python -m pip install --upgrade pip
pip install scikit-build
pip wheel . --verbose
pause