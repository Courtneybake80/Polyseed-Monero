# -*- coding: utf-8 -*-
"""Settings - Development environment setup from README"""

from pathlib import Path

from utils.ui import draw_table, show_tile, print_info


def action_settings():
    """Display development environment setup instructions"""
    headers = ["Step", "Command", "Description"]
    rows = [
        ("1", "git clone https://github.com/tompftampffern/polyseed-monero", "Clone the repository"),
        ("2", "cd polyseed-monero/src", "Enter source directory"),
        ("3", "python build_files.py", "Build static, dynamic lib & executable"),
        ("4", "pip install colorama (for CLI)", "Install CLI dependencies"),
    ]
    draw_table(" DEVELOPMENT ENVIRONMENT ", headers, rows, [6, 55, 35])

    base_dir = Path(__file__).parent.parent
    show_tile(
        f"Project path: {base_dir}\n\n"
        "Recommended: Python 3.8+\n"
        "Windows & macOS: follow manual steps.\n"
        "On macOS: easier DMG download available.",
        "Paths & Tips",
        "#"
    )
    print_info("See README for full build documentation")
