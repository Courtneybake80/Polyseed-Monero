# -*- coding: utf-8 -*-
"""
Polyseed Monero CLI — configuration management.
Handles seed generation parameters, wordlist selection, and cryptographic settings.
"""
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional


_BASE_DIR = Path(__file__).resolve().parent
_CONFIG_FILE = _BASE_DIR / "polyseed_config.json"

SUPPORTED_LANGUAGES = [
    "english", "japanese", "korean", "spanish", "french",
    "italian", "czech", "portuguese", "chinese_simplified", "chinese_traditional",
]

DEFAULT_PBKDF2_ITERATIONS = 10000
DEFAULT_SEED_WORDS = 16
DEFAULT_SECURITY_BITS = 128
DEFAULT_BIRTHDAY_OFFSET_EPOCH = 1635768000


@dataclass
class PolyseedConfig:
    language: str = "english"
    pbkdf2_iterations: int = DEFAULT_PBKDF2_ITERATIONS
    seed_word_count: int = DEFAULT_SEED_WORDS
    security_bits: int = DEFAULT_SECURITY_BITS
    birthday_epoch: int = DEFAULT_BIRTHDAY_OFFSET_EPOCH
    encrypt_by_default: bool = False
    custom_bits: int = 0
    checksum_polynomial: str = "reed_solomon"
    output_format: str = "text"
    verify_after_generate: bool = True
    auto_copy_to_clipboard: bool = False
    log_level: str = "INFO"

    def validate(self) -> list[str]:
        """Return list of validation errors, empty if valid."""
        errors = []
        if self.language not in SUPPORTED_LANGUAGES:
            errors.append(f"Unsupported language: {self.language}")
        if self.seed_word_count != 16:
            errors.append("Polyseed requires exactly 16 words")
        if self.custom_bits < 0 or self.custom_bits > 3:
            errors.append("Custom bits must be 0-3")
        if self.pbkdf2_iterations < 1000:
            errors.append("PBKDF2 iterations must be >= 1000")
        return errors


def load_config() -> PolyseedConfig:
    """Load configuration from disk or return defaults."""
    if not _CONFIG_FILE.exists():
        cfg = PolyseedConfig()
        save_config(cfg)
        return cfg

    with open(_CONFIG_FILE, "r", encoding="utf-8") as fp:
        raw = json.load(fp)

    cfg = PolyseedConfig()
    for k, v in raw.items():
        if hasattr(cfg, k):
            setattr(cfg, k, v)
    return cfg


def save_config(cfg: PolyseedConfig) -> None:
    """Persist configuration to disk."""
    with open(_CONFIG_FILE, "w", encoding="utf-8") as fp:
        json.dump(asdict(cfg), fp, indent=2, ensure_ascii=False)


def reset_config() -> PolyseedConfig:
    """Reset to defaults."""
    cfg = PolyseedConfig()
    save_config(cfg)
    return cfg


def set_language(lang: str) -> Optional[str]:
    """Set wordlist language if supported. Returns error or None."""
    if lang not in SUPPORTED_LANGUAGES:
        return f"Unsupported language '{lang}'. Supported: {', '.join(SUPPORTED_LANGUAGES)}"
    cfg = load_config()
    cfg.language = lang
    save_config(cfg)
    return None
