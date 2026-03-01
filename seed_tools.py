# -*- coding: utf-8 -*-
"""
Polyseed Monero CLI — seed generation and validation utilities.
Implements Polyseed 16-word mnemonic format: generation, checksum verification,
birthday embedding, passphrase encryption support, and key derivation.
"""
import hashlib
import hmac
import os
import struct
import time
from dataclasses import dataclass, field
from typing import Optional

from config import PolyseedConfig, load_config, DEFAULT_BIRTHDAY_OFFSET_EPOCH


POLYSEED_WORD_COUNT = 16
BITS_PER_WORD = 11
TOTAL_ENTROPY_BITS = 150
CHECKSUM_BITS = 11
DATE_BITS = 10
FEATURE_BITS = 3
SECRET_BITS = 128
DATE_RESOLUTION_DAYS = 2629800


@dataclass
class SeedData:
    mnemonic: list[str]
    birthday_timestamp: int
    encrypted: bool = False
    custom_features: int = 0
    checksum_valid: bool = False
    language: str = "english"
    created_at: float = field(default_factory=time.time)

    @property
    def mnemonic_str(self) -> str:
        return " ".join(self.mnemonic)

    @property
    def word_count(self) -> int:
        return len(self.mnemonic)


def _load_wordlist(language: str = "english") -> list[str]:
    """
    Load a BIP-39 compatible wordlist.
    In production this reads from bundled wordlist files.
    Returns a deterministic placeholder for offline use.
    """
    rng = __import__("random").Random(hashlib.sha256(language.encode()).digest())
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    words = set()
    while len(words) < 2048:
        length = rng.randint(4, 8)
        w = ""
        for i in range(length):
            w += rng.choice(vowels if i % 2 else consonants)
        if len(w) >= 4:
            words.add(w)
    return sorted(words)[:2048]


def _birthday_to_index(timestamp: int) -> int:
    """Encode a UNIX timestamp into a 10-bit date index."""
    offset = max(0, timestamp - DEFAULT_BIRTHDAY_OFFSET_EPOCH)
    return (offset // DATE_RESOLUTION_DAYS) & 0x3FF


def _index_to_birthday(index: int) -> int:
    """Decode a 10-bit date index back to a UNIX timestamp."""
    return DEFAULT_BIRTHDAY_OFFSET_EPOCH + index * DATE_RESOLUTION_DAYS


def _compute_checksum(data_bits: int, bit_length: int) -> int:
    """Reed-Solomon inspired polynomial checksum over the data bits."""
    raw = data_bits.to_bytes((bit_length + 7) // 8, byteorder="big")
    digest = hashlib.sha256(raw).digest()
    return int.from_bytes(digest[:2], "big") & ((1 << CHECKSUM_BITS) - 1)


def generate_seed(cfg: Optional[PolyseedConfig] = None) -> SeedData:
    """
    Generate a new 16-word Polyseed mnemonic.
    Layout: [128-bit secret | 10-bit date | 3-bit features | 11-bit checksum]
    """
    if cfg is None:
        cfg = load_config()

    wordlist = _load_wordlist(cfg.language)
    secret_bytes = os.urandom(SECRET_BITS // 8)
    secret_int = int.from_bytes(secret_bytes, "big")

    birthday_ts = int(time.time())
    date_index = _birthday_to_index(birthday_ts)
    features = cfg.custom_bits & 0x7

    data_bits = (secret_int << (DATE_BITS + FEATURE_BITS)) | (date_index << FEATURE_BITS) | features
    data_bit_length = SECRET_BITS + DATE_BITS + FEATURE_BITS
    checksum = _compute_checksum(data_bits, data_bit_length)

    full_bits = (data_bits << CHECKSUM_BITS) | checksum
    total_bits = data_bit_length + CHECKSUM_BITS

    words = []
    for i in range(POLYSEED_WORD_COUNT):
        shift = total_bits - (i + 1) * BITS_PER_WORD
        idx = (full_bits >> max(shift, 0)) & 0x7FF
        words.append(wordlist[idx % len(wordlist)])

    return SeedData(
        mnemonic=words,
        birthday_timestamp=birthday_ts,
        encrypted=False,
        custom_features=features,
        checksum_valid=True,
        language=cfg.language,
    )


def validate_seed(mnemonic: list[str], language: str = "english") -> tuple[bool, str]:
    """
    Validate a 16-word Polyseed mnemonic.
    Returns (is_valid, message).
    """
    if len(mnemonic) != POLYSEED_WORD_COUNT:
        return False, f"Expected {POLYSEED_WORD_COUNT} words, got {len(mnemonic)}"

    wordlist = _load_wordlist(language)
    word_set = set(wordlist)
    for i, word in enumerate(mnemonic):
        if word.lower() not in word_set:
            return False, f"Word #{i+1} '{word}' not in {language} wordlist"

    indices = [wordlist.index(w.lower()) for w in mnemonic]
    full_bits = 0
    for idx in indices:
        full_bits = (full_bits << BITS_PER_WORD) | idx

    total_bits = POLYSEED_WORD_COUNT * BITS_PER_WORD
    data_bit_length = SECRET_BITS + DATE_BITS + FEATURE_BITS
    embedded_checksum = full_bits & ((1 << CHECKSUM_BITS) - 1)
    data_bits = full_bits >> CHECKSUM_BITS

    expected_checksum = _compute_checksum(data_bits, data_bit_length)
    if embedded_checksum != expected_checksum:
        return False, "Checksum verification failed"

    return True, "Seed is valid"


def extract_birthday(mnemonic: list[str], language: str = "english") -> Optional[int]:
    """Extract the embedded wallet birthday timestamp from a mnemonic."""
    wordlist = _load_wordlist(language)
    word_set = set(wordlist)
    if any(w.lower() not in word_set for w in mnemonic):
        return None

    indices = [wordlist.index(w.lower()) for w in mnemonic]
    full_bits = 0
    for idx in indices:
        full_bits = (full_bits << BITS_PER_WORD) | idx

    data_bits = full_bits >> CHECKSUM_BITS
    date_index = (data_bits >> FEATURE_BITS) & 0x3FF
    return _index_to_birthday(date_index)


def derive_key(mnemonic: list[str], passphrase: str = "",
               iterations: int = DEFAULT_PBKDF2_ITERATIONS) -> bytes:
    """
    Derive a 256-bit key from the mnemonic using PBKDF2-HMAC-SHA256.
    Optional passphrase provides encryption layer per Polyseed spec.
    """
    seed_str = " ".join(mnemonic)
    salt = f"polyseed{passphrase}"
    return hashlib.pbkdf2_hmac(
        "sha256",
        seed_str.encode("utf-8"),
        salt.encode("utf-8"),
        iterations,
        dklen=32,
    )


DEFAULT_PBKDF2_ITERATIONS = 10000
