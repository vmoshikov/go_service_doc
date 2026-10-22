"""Конфигурация flow: config.example.json (в git) + config.json (личный, не в git).

config.example.json — командные значения: URL, статусы Jira, JQL, метки, путь к intents, гейты. Секреты пустые.
config.json — личное: роль, токены, OpenAI API, пути к клонам. Любое поле config.json перекрывает поле образца.
Секреты: переменные окружения имеют приоритет над config.json. Это нужно для CI, где config.json нет.

Это модуль, а не скил: префикс «_» исключает его из проверки check_skills.py.
"""
import json
import os
import stat
import subprocess
from pathlib import Path

from _wiki import ROOT

CONFIG = Path(os.environ.get("MK8S_CONFIG", ROOT / "config.json"))
EXAMPLE = ROOT / "config.example.json"

# Ключ в config.json → переменная окружения.
SECRETS = {
    "jira.token": "JIRA_TOKEN",
    "jira.email": "JIRA_EMAIL",
    "gitlab.token": "GITLAB_TOKEN",
    "openai.api_key": "OPENAI_API_KEY",
}

PERSONAL = {"role": "", "jira": {"token": "", "email": ""}, "gitlab": {"token": ""},
            "openai": {"api_key": "", "model": ""}, "repos": {"master-spec": "../master-spec"}}

_cache = None
_personal = None


class ConfigError(SystemExit):
    pass


def tracked_in_git() -> bool:
    if not CONFIG.is_file() or ROOT not in CONFIG.resolve().parents:
        return False
    result = subprocess.run(["git", "ls-files", "--error-unmatch", CONFIG.name], cwd=CONFIG.parent,
                            capture_output=True, text=True)
    return result.returncode == 0


def _read(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Ошибка: {path.name}, строка {exc.lineno}: неверный JSON ({exc.msg})") from None


def _merge(base: dict, override: dict) -> dict:
    result = dict(base)
    for key, value in override.items():
        result[key] = _merge(base[key], value) if isinstance(value, dict) and isinstance(base.get(key), dict) else value
    return result


def personal() -> dict:
    """Только config.json, без значений образца."""
    global _personal
    if _personal is None:
        if CONFIG.is_file() and tracked_in_git():
            raise ConfigError("СТОП. config.json добавлен в git. Ключи в нём считаются скомпрометированными: "
                              "удали файл из git (git rm --cached config.json), отзови и выпусти токены заново.")
        _personal = _read(CONFIG) if CONFIG.is_file() else {}
    return _personal


def load() -> dict:
    """config.example.json, перекрытый config.json."""
    global _cache
    if _cache is None:
        if not EXAMPLE.is_file():
            raise ConfigError(f"Ошибка: нет {EXAMPLE.name} в корне репозитория")
        _cache = _merge(_read(EXAMPLE), personal())
    return _cache


def save(data: dict) -> None:
    """Пишет личный config.json с правами 600."""
    global _cache, _personal
    CONFIG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    CONFIG.chmod(0o600)
    _cache, _personal = None, data


def init_personal() -> dict:
    """Создаёт config.json с личными полями, если файла нет."""
    if not CONFIG.is_file():
        save(json.loads(json.dumps(PERSONAL)))
    return personal()


def get(dotted: str, default=None):
    data = load()
    for part in dotted.split("."):
        if not isinstance(data, dict) or part not in data:
            return default
        data = data[part]
    return data if data not in ("", None) else default


def secret(dotted: str) -> str:
    """Секрет из окружения или config.json. Значение никогда не выводится."""
    env = SECRETS[dotted]
    value = os.environ.get(env, "").strip() or str(get(dotted, "")).strip()
    if not value:
        raise ConfigError(f"Ошибка: нет «{dotted}» в {CONFIG.name} и нет переменной окружения {env}. "
                          f"Заполни {CONFIG.name} по образцу config.example.json.")
    return value


def permissions_ok() -> bool:
    if not CONFIG.is_file():
        return True
    return not CONFIG.stat().st_mode & (stat.S_IRWXG | stat.S_IRWXO)


def repo(name: str):
    """Путь к локальному клону из раздела repos или None. Относительный путь — от корня репозитория."""
    raw = get(f"repos.{name}")
    if not raw:
        return None
    path = Path(os.path.expanduser(raw))
    return (path if path.is_absolute() else ROOT / path).resolve()


def cache_dir() -> Path:
    return Path(os.path.expanduser(get("cache_dir", "~/.cache/mk8s-flow"))).resolve()


def openai() -> dict:
    """Настройки OpenAI-совместимого API: api_key, base_url, model."""
    return {"api_key": secret("openai.api_key"),
            "base_url": get("openai.base_url", "https://api.openai.com/v1"),
            "model": get("openai.model", "")}
