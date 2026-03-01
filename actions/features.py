# -*- coding: utf-8 -*-
"""Features - Polyseed main features from README"""

from utils.ui import draw_table, show_tile, print_info


def action_features():
    """Display main Polyseed features"""
    headers = ["Feature", "Description"]
    rows = [
        ("16 mnemonic words", "36% shorter than original 25-word seed"),
        ("Wallet birthday", "Embedded to optimize seed restoration"),
        ("Passphrase encryption", "Supports optional encryption"),
        ("3 custom bits", "Can store up to 3 custom bits"),
        ("Polynomial checksum", "Reed-Solomon error correction code"),
        ("Coin incompatibility", "Seeds incompatible between different coins"),
    ]
    draw_table(" FEATURES ", headers, rows, [22, 45])

    show_tile(
        "128-bit security level (ed25519 curve).\n"
        "PBKDF2-HMAC-SHA256 with 10000 iterations.\n"
        "Dates from Nov 2021 to Feb 2107 supported.",
        "Security & Compatibility"
    )
    print_info("See Encoding menu for word structure details")
