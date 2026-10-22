"""Поиск секретов и персональных данных в тексте. Найденное значение не возвращается.

Это модуль, а не скил: префикс «_» исключает его из проверки check_skills.py.
"""
import re

# Значения-заглушки вида <TOKEN> и $VAR не считаются секретами.
SECRET_PATTERNS = [
    ("приватный ключ", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("kubeconfig: ключ или токен",
     re.compile(r"\b(?:client-key-data|client-certificate-data|token)\s*:\s*(?![<$])[A-Za-z0-9+/=._-]{20,}")),
    ("Bearer-токен", re.compile(r"Bearer\s+(?![<$])[A-Za-z0-9._-]{20,}")),
    ("пароль", re.compile(r"(?i)\b(?:password|passwd|пароль)\s*[:=]\s*(?![<$`*])\S{6,}")),
    ("ключ AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("токен GitLab", re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}")),
]

PII_PATTERNS = [
    ("email", re.compile(r"\b[\w.+-]+@(?!example\.(?:com|org|net)\b)[\w-]+(?:\.[\w-]+)+\b")),
    ("телефон", re.compile(r"(?:\+7|\b8)[\s(-]*(?!000)\d{3}[\s)-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}\b")),
    ("СНИЛС", re.compile(r"\b\d{3}-\d{3}-\d{3}[\s-]\d{2}\b")),
]
CARD = re.compile(r"\b(?:\d[ -]?){15,18}\d\b")


def _luhn(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2:
            d = d * 2 - 9 if d > 4 else d * 2
        total += d
    return total % 10 == 0


def scan(text: str, pii: bool = True) -> list:
    """[(номер строки, тип)] для каждой находки."""
    found = []
    patterns = SECRET_PATTERNS + (PII_PATTERNS if pii else [])
    for number, line in enumerate(text.splitlines(), start=1):
        for kind, pattern in patterns:
            if pattern.search(line):
                found.append((number, kind))
        if pii and any(_luhn(m.group()) for m in CARD.finditer(line)):
            found.append((number, "номер карты"))
    return found
