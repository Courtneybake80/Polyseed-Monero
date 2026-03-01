@echo off
chcp 65001 >nul
title Polyseed Monero - CLI
color 0C
cd /d "%~dp0"
python -c "import colorama" 2>nul || pip install colorama -q
python main.py
pause
