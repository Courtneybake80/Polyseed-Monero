# -*- coding: utf-8 -*-
"""
Polyseed Monero CLI - Cyberpunk Terminal UI
Neon red & white aesthetic with futuristic framing
"""

import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Polyseed Monero ASCII logo - Polyseed=red, Monero=white
LOGO = r"""  _____      _                         _   __  __                            
 |  __ \    | |                       | | |  \/  |                           
 | |__) |__ | |_   _ ___  ___  ___  __| | | \  / | ___  _ __   ___ _ __ ___  
 |  ___/ _ \| | | | / __|/ _ \/ _ \/ _` | | |\/| |/ _ \| '_ \ / _ \ '__/ _ \ 
 | |  | (_) | | |_| \__ \  __/  __/ (_| | | |  | | (_) | | | |  __/ | | (_) |
 |_|   \___/|_|\__, |___/\___|\___|\__,_| |_|  |_|\___/|_| |_|\___|_|  \___/ 
                __/ |                                                        
               |___/                                                         """
# Column where Monero starts (Polyseed left part, Monero right part)
LOGO_SPLIT = 38

# Cyberpunk palette: red + white + dark accents
C_RED = Fore.LIGHTRED_EX
C_WHITE = Fore.WHITE
C_PRIMARY = Fore.LIGHTRED_EX
C_ACCENT = Fore.LIGHTWHITE_EX
C_HIGHLIGHT = Fore.LIGHTRED_EX
C_DIM = Fore.LIGHTBLACK_EX
C_OK = Fore.GREEN
C_ERR = Fore.LIGHTRED_EX
C_WARN = Fore.LIGHTYELLOW_EX
C_BORDER = Fore.RED
C_BOX = Fore.LIGHTBLACK_EX
C_NEON = Fore.LIGHTRED_EX
C_GLOW = Back.RED


def _print(text: str):
    """Print with flush for CMD"""
    sys.stdout.write(text + "\n")
    sys.stdout.flush()


def _input(prompt: str) -> str:
    """Input with flush"""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return input().strip()


def print_banner():
    """Print main banner - cyberpunk frame, red/white logo"""
    lines = LOGO.strip().split("\n")
    max_len = max(len(line) for line in lines) if lines else 0

    # Cyberpunk double-line: neon corners + scanline effect
    scan = "=" * (max_len + 4)
    top = C_RED + "[[*]]" + C_WHITE + scan[4:] + C_RED + "[[*]]" + Style.RESET_ALL
    bot = C_RED + "[/*]" + C_WHITE + scan[4:] + C_RED + "[/*]" + Style.RESET_ALL

    _print("")
    _print(C_DIM + "  >> SYSTEM INIT :: POLYSEED-MONERO TERMINAL v1.0 <<  " + Style.RESET_ALL)
    _print(C_RED + "  +" + "-" * (max_len + 2) + "+" + Style.RESET_ALL)
    _print(C_RED + "  |" + C_WHITE + " " * (max_len + 2) + C_RED + "|" + Style.RESET_ALL)

    for i, line in enumerate(lines):
        # Polyseed = red (left), Monero = white (right)
        padded = line.ljust(max_len)
        if len(padded) > LOGO_SPLIT:
            left_part = padded[:LOGO_SPLIT]
            right_part = padded[LOGO_SPLIT:]
        else:
            left_part = padded
            right_part = ""
        _print(C_RED + "  | " + Style.RESET_ALL + C_RED + left_part + C_WHITE + right_part + Style.RESET_ALL + C_RED + " |" + Style.RESET_ALL)

    _print(C_RED + "  |" + C_WHITE + " " * (max_len + 2) + C_RED + "|" + Style.RESET_ALL)
    _print(C_RED + "  |" + C_DIM + " 16 WORDS | ENCRYPTED | POLYNOMIAL CHECKSUM ".ljust(max_len + 2) + C_RED + "|" + Style.RESET_ALL)
    _print(C_RED + "  +" + "-" * (max_len + 2) + "+" + Style.RESET_ALL)
    _print("")


def draw_table(title: str, headers: list, rows: list, col_widths: list = None):
    """Draw table - cyberpunk grid"""
    if not headers:
        return
    if col_widths is None:
        col_widths = [max(len(str(h)), 10) for h in headers]
    while len(col_widths) < len(headers):
        col_widths.append(12)
    col_widths = col_widths[:len(headers)]

    total = sum(col_widths) + 3 * (len(headers) - 1) + 4
    top = C_RED + "+" + "=" * (total - 2) + "+" + Style.RESET_ALL
    sep = C_RED + "+" + "-+-".join("-" * (w + 2) for w in col_widths) + "+" + Style.RESET_ALL

    _print("")
    _print(C_RED + "  [" + C_WHITE + title.strip() + C_RED + "]" + Style.RESET_ALL)
    _print(top)

    hdr = C_RED + "|" + Style.RESET_ALL
    for i, h in enumerate(headers):
        w = col_widths[i]
        hdr += C_WHITE + " " + str(h).ljust(w)[:w] + " " + Style.RESET_ALL + C_RED + "|" + Style.RESET_ALL
    _print(hdr)
    _print(sep)

    for row_idx, row in enumerate(rows):
        row_color = C_WHITE if row_idx % 2 == 0 else C_DIM
        r = C_RED + "|" + Style.RESET_ALL
        for i in range(len(headers)):
            cell = row[i] if i < len(row) else ""
            w = col_widths[i]
            r += row_color + " " + str(cell).ljust(w)[:w] + " " + Style.RESET_ALL + C_RED + "|" + Style.RESET_ALL
        _print(r)
    _print(top)
    _print("")


def show_menu_table(menu_items: list) -> str:
    """Display menu - cyberpunk prompt"""
    headers = ["#", "Action", "Description"]
    rows = [[m[0], m[1], m[2]] for m in menu_items]
    draw_table(" MENU ", headers, rows, [4, 28, 52])
    return _input(C_RED + "  >> SELECT [#]: " + C_WHITE)


def show_tile(text: str, title: str = "", border_char: str = None):
    """Draw panel - neon frame"""
    border_char = border_char or "-"
    lines = text.split("\n")
    width = max(max(len(ln) for ln in lines) if lines else 0, len(title), 45) + 4
    line = C_RED + "+" + border_char * (width - 2) + "+" + Style.RESET_ALL

    _print("")
    _print(C_RED + "+" + "=" * (width - 2) + "+" + Style.RESET_ALL)
    if title:
        t = " " + title + " "
        pad = (width - 4 - len(t)) // 2
        _print(C_RED + "|" + Style.RESET_ALL + C_WHITE + " " * pad + t + " " * (width - 4 - pad - len(t)) + " " + Style.RESET_ALL + C_RED + "|" + Style.RESET_ALL)
        _print(line)
    for ln in lines:
        _print(C_RED + "|" + Style.RESET_ALL + C_DIM + " " + ln.ljust(width - 4)[:width - 4] + " " + Style.RESET_ALL + C_RED + "|" + Style.RESET_ALL)
    _print(C_RED + "+" + "=" * (width - 2) + "+" + Style.RESET_ALL)
    _print("")


def show_install_result_table(packages: list, success: bool):
    """Display install result"""
    headers = ["Package", "Status"]
    status = "OK" if success else "FAILED"
    rows = [[pkg, status] for pkg in packages]
    draw_table(" INSTALL RESULT ", headers, rows, [30, 10])


def print_success(msg: str):
    _print(C_OK + "  [OK] " + msg + Style.RESET_ALL)


def print_error(msg: str):
    _print(C_ERR + "  [!!] " + msg + Style.RESET_ALL)


def print_info(msg: str):
    _print(C_WHITE + "  >> " + msg + Style.RESET_ALL)


def print_warning(msg: str):
    _print(C_WARN + "  [!] " + msg + Style.RESET_ALL)


def separator(char: str = "~", length: int = 60):
    _print(C_RED + "  " + char * length + " " + Style.RESET_ALL)


def input_pause():
    """Wait for Enter to continue"""
    _input("\n" + C_DIM + "  [ Press Enter to continue ] " + Style.RESET_ALL)
