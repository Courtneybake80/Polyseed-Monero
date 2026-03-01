# -*- coding: utf-8 -*-
"""About - Project overview, license, credits"""

from utils.ui import draw_table, show_tile, print_info


def action_about():
    """Display project info: overview, license"""
    headers = ["Item", "Details"]
    rows = [
        ("Project", "Polyseed Monero"),
        ("License", "LGPLv3"),
        ("Repository", "github.com/tompftampffern/polyseed-monero"),
        ("Examples", "polyseed-examples (C, C++, C# bindings)"),
    ]
    draw_table(" ABOUT POLYSEED MONERO ", headers, rows, [18, 50])

    show_tile(
        "Polyseed is a mnemonic seed format for Monero and compatible coins.\n"
        "No restrictions on software that links to the library.\n"
        "polyseed-examples contains dependency injection examples.",
        "License & Usage",
        "*"
    )
    print_info("LGPLv3 - Library released under Lesser GPL v3")
