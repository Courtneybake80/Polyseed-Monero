#!/bin/bash
cd "$(dirname "$0")"
python3 -c "import colorama" 2>/dev/null || pip install colorama -q
python3 main.py
read -p "Press Enter to continue..."
