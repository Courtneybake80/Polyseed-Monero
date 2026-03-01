# -*- coding: utf-8 -*-
"""API - API and dependency injection from README"""

from utils.ui import draw_table, show_tile, print_info


def action_api():
    """Display API and dependency injection info"""
    headers = ["Dependency", "Description", "Implemented In"]
    rows = [
        ("randbytes", "Generate cryptographically secure random bytes", "libsodium, OpenSSL"),
        ("pbkdf2_sha256", "Calculate PBKDF2 HMAC-SHA256", "libsodium, OpenSSL"),
        ("memzero", "Securely erase memory", "libsodium, OpenSSL"),
        ("u8_nfc", "UTF8 to composed canonical form", "Boost.Locale, utf8proc"),
        ("u8_nfkd", "UTF8 to decomposed canonical form", "Boost.Locale, utf8proc"),
    ]
    draw_table(" DEPENDENCY INJECTION (REQUIRED) ", headers, rows, [15, 35, 25])

    headers2 = ["Dependency", "Description", "Libc Function"]
    rows2 = [
        ("time", "Get current unix time", "uint64_t time(void);"),
        ("alloc", "Allocate memory", "void* malloc(size_t size);"),
        ("free", "Free memory", "void free(void* ptr);"),
    ]
    draw_table(" OPTIONAL DEPENDENCIES ", headers2, rows2, [12, 25, 30])

    show_tile(
        "API documented in polyseed.h\n"
        "Call polyseed_inject() to provide the 5 required functions.\n"
        "polyseed-examples has C, C++, C# examples.",
        "API Documentation"
    )
    print_info("polyseed doesn't contain cryptographic code - reduces security risk")
