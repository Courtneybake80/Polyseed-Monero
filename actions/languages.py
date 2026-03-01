# -*- coding: utf-8 -*-
"""Supported Languages - Polyseed wordlists from README"""

from utils.ui import draw_table, show_tile, print_info


def action_languages():
    """Display supported languages"""
    headers = ["Language", "Code", "Notes"]
    rows = [
        ("English", "en", "Default"),
        ("Japanese", "ja", ""),
        ("Korean", "ko", ""),
        ("Spanish", "es", "Accents optional"),
        ("French", "fr", "Accents optional"),
        ("Italian", "it", ""),
        ("Czech", "cs", ""),
        ("Portuguese", "pt", ""),
        ("Chinese (Simplified)", "zh-Hans", ""),
        ("Chinese (Traditional)", "zh-Hant", ""),
    ]
    draw_table(" SUPPORTED LANGUAGES ", headers, rows, [22, 12, 20])

    show_tile(
        "Latin alphabet: only first 4 characters of each word needed when restoring.\n"
        "French & Spanish: input with or without accents.\n"
        "Wordlists based on BIP-39 with minor changes.",
        "Restoration Tips"
    )
    print_info("10 languages supported for mnemonic generation and restoration")
