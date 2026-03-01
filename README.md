# Polyseed-Monero
Polyseed Monero CLI — Command-line reference tool for Polyseed 16-word mnemonic documentation and Monero wallet seed utilities with key derivation reference, birthday encoding, language support (IETF BCP-47), error correction, and Rich terminal interface for XMR privacy tools
<div align="center">

```
  _____      _                         _   __  __
 |  __ \    | |                       | | |  \/  |
 | |__) |__ | |_   _ ___  ___  ___  __| | | \  / | ___  _ __   ___ _ __ ___
 |  ___/ _ \| | | | / __|/ _ \/ _ \/ _` | | |\/| |/ _ \| '_ \ / _ \ '__/ _ \
 | |  | (_) | | |_| \__ \  __/  __/ (_| | | |  | | (_) | | | |  __/ | | (_) |
 |_|   \___/|_|\__, |___/\___|\___|\__,_| |_|  |_|\___/|_| |_|\___|_|  \___/
                __/ |
               |___/
```

# Polyseed Monero CLI

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-LGPLv3-blue?style=for-the-badge)](LICENSE)
[![Monero](https://img.shields.io/badge/Monero-XMR-FF6600?style=for-the-badge&logo=monero)](https://www.getmonero.org/)
[![Polyseed](https://img.shields.io/badge/Polyseed-16--word-00D4AA?style=for-the-badge)](https://github.com/tevador/polyseed)

**CLI for Polyseed mnemonic documentation and Monero wallet seed tools**

[Features](#features) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [Project Structure](#project-structure) • [FAQ](#faq)

</div>

---

## Official Links

| Resource | URL |
|----------|-----|
| **Monero** | https://www.getmonero.org |
| **Polyseed Specification** | https://github.com/tevador/polyseed |
| **Polyseed in Monero Docs** | https://docs.getmonero.org/mnemonics/polyseed/ |
| **polyseed-monero (C Library)** | https://github.com/tompftampffern/polyseed-monero |
| **Monero Mnemonics Overview** | https://docs.getmonero.org/mnemonics/ |
| **Feather Wallet** | https://featherwallet.org |

---

## Features

<table>
<tr>
<td width="50%">

| Feature | ✓ |
|---------|---|
| Install Dependencies (pip) | ✓ |
| Build instructions for polyseed-monero | ✓ |
| 16-word mnemonic documentation | ✓ |
| Polynomial checksum (Reed-Solomon) | ✓ |
| Passphrase encryption support | ✓ |
| Up to 3 custom feature bits | ✓ |
| Embedded wallet birthday | ✓ |
| Coin incompatibility (XMR-only) | ✓ |

</td>
<td width="50%">

| Feature | ✓ |
|---------|---|
| 10 languages (BIP-39 wordlists) | ✓ |
| Encoding structure reference | ✓ |
| API & dependency injection guide | ✓ |
| Development environment setup | ✓ |
| Terminal UI | ✓ |
| Static/dynamic library build info | ✓ |
| LGPLv3 licensed | ✓ |
| Windows & Unix support | ✓ |

</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

- **Python** 3.8 or higher
- **pip** (Python package manager)

### Installation

**Windows (one-click):**

```batch
run.bat
```

**Manual (all platforms):**

```bash
# Clone the repository
git clone https://github.com/xmr-utils/Polyseed-Monero-CLI.git
cd Polyseed-Monero-CLI

# Install dependencies
pip install -r requirements.txt

# Run the CLI
python main.py
```

**Unix (Linux/macOS):**

```bash
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| colorama | ≥0.4.6 | Cross-platform colored terminal output |

---

## Configuration

The CLI uses environment variables for development and optional paths. Create a `.env` file in the project root or export before running:

```bash
# Optional: Path to polyseed-monero source (for build instructions reference)
POLYSEED_MONERO_PATH=/path/to/polyseed-monero

# Optional: Force UTF-8 on Windows (run.bat sets chcp 65001)
PYTHONIOENCODING=utf-8
```

For building the underlying **polyseed-monero** C library, configure:

```bash
# Clone and build polyseed-monero
git clone https://github.com/tompftampffern/polyseed-monero
cd polyseed-monero/src
python build_files.py
```

> **Tip:** The CLI is a documentation tool. To generate or restore seeds, use the polyseed-monero library or wallets like Feather Wallet.

---

## Usage

Interactive menu-driven interface. After launching, select an option by number:

```
  +============================================================+
  | #   | Action                 | Description                 |
  +-----+------------------------+-----------------------------+
  | 1   | Install Dependencies   | pip install -r requirements |

  | 2   | Build                  | Clone & build polyseed-monero (static/dynamic lib) |
  | 3   | Features               | 16 words, checksum, encryption, custom bits |
  | 4   | Supported Languages    | 10 languages (BIP-39 based wordlists) |
  | 5   | Encoding               | Word structure, checksum, feature bits |
  | 6   | API & Dependency Inj.  | polyseed.h, randbytes, pbkdf2, etc. |
  | 7   | Settings               | Development environment setup |
  | 8   | About                  | License LGPLv3, repository, credits |
  | 0   | Exit                   | Quit the application |
  +============================================================+

  >> SELECT [#]: _
```

---

## Project Structure

```
Polyseed-Monero-CLI/
├── main.py              # Entry point, menu loop
├── requirements.txt     # Python dependencies (colorama)
├── run.bat              # Windows launcher (chcp 65001, auto-install)
├── run.sh               # Unix launcher (bash)
├── actions/
│   ├── __init__.py
│   ├── about.py         # License, credits, repository info
│   ├── api.py           # polyseed.h, dependency injection
│   ├── build.py         # polyseed-monero build instructions
│   ├── encoding.py      # Word structure, checksum, feature bits
│   ├── features.py      # 16 words, birthday, encryption
│   ├── install.py       # pip install -r requirements.txt
│   ├── languages.py     # 10 supported languages
│   └── settings.py      # Development environment setup
└── utils/
    ├── __init__.py
    └── ui.py            # Terminal UI, tables, banners
```

---

## FAQ

<details>
<summary><strong>What is Polyseed?</strong></summary>

Polyseed is a modern mnemonic scheme for Monero wallets. It uses **16 words** (36% shorter than the legacy 25-word format), embeds the wallet birthday for restore-height optimization, supports passphrase encryption, and includes a polynomial checksum (Reed-Solomon). Designed for 128-bit security level matching ed25519.
</details>

<details>
<summary><strong>Does this CLI generate or restore seeds?</strong></summary>

No. This CLI is a **documentation and reference tool** for the Polyseed format. It shows features, encoding structure, build instructions, and API information. To generate or restore seeds, use the [polyseed-monero](https://github.com/tompftampffern/polyseed-monero) library or wallets like [Feather Wallet](https://featherwallet.org).
</details>

<details>
<summary><strong>Does this CLI work with the polyseed-monero C library?</strong></summary>

The CLI documents the polyseed-monero library and provides build instructions. It does not link to or call the library directly. To use the library, clone it and build it separately; the CLI's "Build" menu shows the steps.
</details>

<details>
<summary><strong>Which languages are supported for Polyseed?</strong></summary>

English, Japanese, Korean, Spanish, French, Italian, Czech, Portuguese, Chinese (Simplified), and Chinese (Traditional). For Latin-alphabet languages, only the first 4 characters of each word are required when restoring.
</details>

<details>
<summary><strong>Why does run.bat change the code page?</strong></summary>

`chcp 65001` sets the Windows console to UTF-8 for correct display of non-ASCII characters (e.g. in language wordlists). The CLI uses colorama for cross-platform compatibility.
</details>

<details>
<summary><strong>What is the wallet birthday in Polyseed?</strong></summary>

The mnemonic stores the approximate creation date (10 bits, ~1/12 year resolution). Dates from November 2021 to February 2107 are supported. This allows wallet software to scan only relevant blocks during restore instead of from genesis.
</details>

<details>
<summary><strong>Is Polyseed compatible with the old 25-word format?</strong></summary>

No. Polyseed is a separate format. The legacy 25-word Monero seed and Polyseed are incompatible. You cannot convert between them; each format has its own encoding and checksum.
</details>

---

## Disclaimer

This is a **documentation and reference tool** for the Polyseed mnemonic format. It does not generate, store, or process cryptographic seeds or private keys. Use this software at your own risk. For actual wallet operations, use the official [polyseed-monero](https://github.com/tompftampffern/polyseed-monero) library or wallets such as [Feather Wallet](https://featherwallet.org). Never share your seed phrase or private keys. This project is not affiliated with the Monero project or Tevador's Polyseed specification.

---

<div align="center">

**Support Monero development**

If this tool was useful, consider donating XMR:

```
42rGfW3bSCMniDKfVZJz9MXC4uXnPNSzTYcpQnMHVi8r5VUGzJdEQthCJdPVS63oy3XfWk4kPZRGKsQ4LsfV5DgNM6ybHt
```

[![Star on GitHub](https://img.shields.io/badge/Star_on_GitHub-⭐-yellow?style=for-the-badge)](https://github.com/xmr-utils/Polyseed-Monero-CLI)

</div>
