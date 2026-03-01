# -*- coding: utf-8 -*-
"""
Polyseed Monero - CLI
16-word mnemonic seed for Monero | Features | Build | API | Languages
"""

import sys
from utils import ensure_env
from utils.ui import print_banner, print_error, print_info, show_menu_table, input_pause
from actions.install import action_install_dependencies
from actions.settings import action_settings
from actions.about import action_about
from actions.features import action_features
from actions.build import action_build
from actions.api import action_api
from actions.languages import action_languages
from actions.encoding import action_encoding


MENU_ITEMS = [
    ("1", "Install Dependencies", "pip install -r requirements.txt"),
    ("2", "Build", "Clone & build polyseed-monero (static/dynamic lib)"),
    ("3", "Features", "16 words, checksum, encryption, custom bits"),
    ("4", "Supported Languages", "10 languages (BIP-39 based wordlists)"),
    ("5", "Encoding", "Word structure, checksum, feature bits"),
    ("6", "API & Dependency Injection", "polyseed.h, randbytes, pbkdf2, etc."),
    ("7", "Settings", "Development environment setup"),
    ("8", "About", "License LGPLv3, repository, credits"),
    ("0", "Exit", "Quit the application"),
]


@ensure_env
def main():
    print_banner()

    while True:
        choice = show_menu_table(MENU_ITEMS)

        if choice == "0":
            print_info("Goodbye!")
            sys.exit(0)
        elif choice == "1":
            action_install_dependencies()
        elif choice == "2":
            action_build()
        elif choice == "3":
            action_features()
        elif choice == "4":
            action_languages()
        elif choice == "5":
            action_encoding()
        elif choice == "6":
            action_api()
        elif choice == "7":
            action_settings()
        elif choice == "8":
            action_about()
        else:
            print_error("Invalid choice. Enter 0-8.")

        input_pause()


if __name__ == "__main__":
    main()
