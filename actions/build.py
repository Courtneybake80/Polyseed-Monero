# -*- coding: utf-8 -*-
"""Build - Installation and build instructions from README"""

from utils.ui import draw_table, show_tile, print_info


def action_build():
    """Display build and install instructions"""
    headers = ["Step", "Command", "Description"]
    rows = [
        ("1", "git clone https://github.com/tompftampffern/polyseed-monero", "Clone repository"),
        ("2", "cd polyseed-monero/src", "Enter source directory"),
        ("3", "python build_files.py", "Build static lib, dynamic lib, executable"),
    ]
    draw_table(" BUILD INSTRUCTIONS ", headers, rows, [6, 55, 40])

    show_tile(
        "This builds:\n"
        "  - Static library\n"
        "  - Dynamic library\n"
        "  - Executable with functional tests\n\n"
        "Windows & macOS: follow manual steps.\n"
        "macOS: easier DMG download available.",
        "Build Output"
    )
    print_info("Choose manual steps for Windows & macOS users")
