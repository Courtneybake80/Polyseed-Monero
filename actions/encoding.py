# -*- coding: utf-8 -*-
"""Encoding - Word structure and checksum from README"""

from utils.ui import draw_table, show_tile, print_info


def action_encoding():
    """Display encoding structure and checksum info"""
    headers = ["Word #", "Contents"]
    rows = [
        ("1", "Checksum (11 bits)"),
        ("2-6", "Secret seed (10 bits) + features (1 bit)"),
        ("7-16", "Secret seed (10 bits) + birthday (1 bit)"),
    ]
    draw_table(" ENCODING STRUCTURE ", headers, rows, [10, 40])

    show_tile(
        "Each word = 11 bits.\n"
        "Total: 11 checksum + 150 secret + 5 feature + 10 birthday bits.\n"
        "Feature/birthday bits spread over 15 data words.",
        "Bit Allocation"
    )

    headers2 = ["Topic", "Details"]
    rows2 = [
        ("Checksum", "Polynomial over GF(2048), Reed-Solomon error correction"),
        ("Coin flag", "XORed with word 2 - prevents wrong-coin usage"),
        ("Feature bits", "5 total: 2 internal, 3 reserved (must be zero)"),
        ("Wallet birthday", "Resolution ~1/12 year, Nov 2021 - Feb 2107"),
    ]
    draw_table(" CHECKSUM & FEATURES ", headers2, rows2, [18, 55])

    print_info("Single-word errors detected; single-word erasures corrected without false positives")
