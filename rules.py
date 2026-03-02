"""
Rules loader.

Priority:
1) DEFAULT_RULES (built-in)
2) ./rules/<repo_name>.json (repo-specific override)
3) RULES.md json-block (legacy/backward compatible)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


DEFAULT_RULES: Dict[str, Any] = {
    "language": "ru",
    # Directories to exclude from analysis (paths relative to repo root). Example: ["vendor", "third_party", "generated"]
    "exclude_dirs": ["vendor"],
    # Functions doc grouping: 1 = by top-level dir, 2 = by two path levels, 0 or null = by full parent dir of each file
    "functions_group_depth": 2,
    "features": {
        # If true, major sections in main README are rendered as menus only (links to detailed files)
        "thin_readme": True,
        # If true, add emoji to generated menus/links where applicable
        "emoji": True,
        # Import enrichment: clone external git repos and extract types (best effort)
        "import_clone": {
            "enabled": False,
            "max_repos": 8,
            # Optional allowlist of hosts (e.g. ["github.com", "gitlab.com"])
            "hosts": [],
            # Optional overrides for non-standard VCS mappings:
            # {"golang.org/x/net": {"clone_url": "https://go.googlesource.com/net", "repo_root": "golang.org/x/net"}}
            "overrides": {},
        },
    },
    "conflicts": {
        # imports vs libraries: keep exactly one if both enabled/disabled
        # allowed values: "prefer_imports", "prefer_libraries"
        "imports_vs_libraries": "prefer_imports",
    },
    "sections": {
        "architecture_user": {"enabled": True, "source": "user"},
        "db_user": {"enabled": False, "source": "user"},
        "diagrams": {"enabled": True, "source": "auto"},
        "imports": {"enabled": True, "source": "auto"},
        "structures": {"enabled": True, "source": "auto"},
        "functions": {"enabled": True, "source": "auto"},
        "api": {"enabled": True, "source": "auto"},
        "tests": {"enabled": True, "source": "auto"},
        "libraries": {"enabled": True, "source": "auto"},
        "others_user": {"enabled": True, "source": "user"},
    },
    "readme_order": [
        "architecture_user",
        "db_user",
        "diagrams",
        "imports",
        "structures",
        "functions",
        "api",
        "tests",
        "libraries",
        "others_user",
    ],
    "changelog": {
        # Формировать changelog только по веткам (merge-коммиты в теге). 1 ветка = 1 задача = 1 пункт.
        "branches_only": True,
        # Паттерн ключа задачи (форма: ключ-число). Извлекается из имени ветки.
        # Примеры: ABC-123, JIRA-456. Регулярное выражение, группа захвата — первый найденный ключ.
        "task_key_pattern": r"[A-Z][A-Z0-9]+-\d+",
        # Маппинг префикса ветки -> категория changelog (Добавлено/Изменено/Удалено/Исправлено)
        "branch_prefix_to_category": {
            "feature/": "Добавлено",
            "feat/": "Добавлено",
            "bugfix/": "Исправлено",
            "fix/": "Исправлено",
            "hotfix/": "Исправлено",
            "release/": "Изменено",
            "refactor/": "Изменено",
            "remove/": "Удалено",
            "revert/": "Удалено",
        },
        # URL трекера задач для ссылок. Если пусто — JIRA_BASE_URL из env.
        "task_tracker_url": None,
    },
}


def _extract_first_json_block(md_text: str) -> Optional[str]:
    # ```json
    # { ... }
    # ```
    m = re.search(r"```json\s*([\s\S]*?)\s*```", md_text, re.IGNORECASE)
    return m.group(1) if m else None


def _merge_rules(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(base)
    # merge top-level keys except sections/features/conflicts/changelog (handled separately)
    merged.update({k: v for k, v in override.items() if k not in ("sections", "features", "conflicts", "changelog")})

    changelog = dict(base.get("changelog") or {})
    changelog.update(override.get("changelog") or {})
    merged["changelog"] = changelog

    # merge features (deep-ish)
    features = dict(base.get("features", {}))
    ov_features = override.get("features", {}) or {}
    for k, v in ov_features.items():
        if k == "import_clone" and isinstance(v, dict):
            ic = dict(features.get("import_clone", {}))
            ic.update(v)
            features["import_clone"] = ic
        else:
            features[k] = v
    merged["features"] = features

    # merge conflicts
    conflicts = dict(base.get("conflicts", {}))
    conflicts.update(override.get("conflicts", {}) or {})
    merged["conflicts"] = conflicts

    sections = dict(base.get("sections", {}))
    sections.update(override.get("sections", {}) or {})
    merged["sections"] = sections
    return merged


def load_rules_from_md(rules_md_path: Path) -> Dict[str, Any]:
    """Load rules from RULES.md json-block (legacy)."""
    try:
        if not rules_md_path.exists():
            return dict(DEFAULT_RULES)
        text = rules_md_path.read_text(encoding="utf-8")
        block = _extract_first_json_block(text)
        if not block:
            return dict(DEFAULT_RULES)
        parsed = json.loads(block)
        return _merge_rules(dict(DEFAULT_RULES), parsed)
    except Exception:
        return dict(DEFAULT_RULES)


def load_rules_from_json(rules_json_path: Path) -> Dict[str, Any]:
    """Load rules from a JSON file."""
    try:
        if not rules_json_path.exists():
            return dict(DEFAULT_RULES)
        parsed = json.loads(rules_json_path.read_text(encoding="utf-8"))
        return _merge_rules(dict(DEFAULT_RULES), parsed)
    except Exception:
        return dict(DEFAULT_RULES)


def load_rules_for_repo(repo_name: str, base_dir: Path) -> Tuple[Dict[str, Any], Optional[Path]]:
    """
    Load rules for a repository.

    Returns: (rules, source_path_used)
    """
    # Default rules first
    rules = dict(DEFAULT_RULES)

    # Repo-specific JSON override
    repo_rules_json = (base_dir / "rules" / f"{repo_name}.json")
    if repo_rules_json.exists():
        return load_rules_from_json(repo_rules_json), repo_rules_json

    # Legacy: RULES.md in base_dir
    legacy_md = base_dir / "RULES.md"
    if legacy_md.exists():
        return load_rules_from_md(legacy_md), legacy_md

    return rules, None


def normalize_rules(rules: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply normalization & conflict resolution so config is safe to use.

    - imports vs libraries are mutually exclusive by default: keep exactly one.
    """
    try:
        strategy = (rules.get("conflicts") or {}).get("imports_vs_libraries", "prefer_imports")
    except Exception:
        strategy = "prefer_imports"

    imports_on = is_enabled(rules, "imports")
    libs_on = is_enabled(rules, "libraries")

    # If both enabled -> disable one (keep exactly one)
    if imports_on and libs_on:
        if strategy == "prefer_libraries":
            rules.setdefault("sections", {}).setdefault("imports", {})["enabled"] = False
        else:
            rules.setdefault("sections", {}).setdefault("libraries", {})["enabled"] = False

    # If both disabled -> enable one (keep exactly one)
    if (not is_enabled(rules, "imports")) and (not is_enabled(rules, "libraries")):
        if strategy == "prefer_libraries":
            rules.setdefault("sections", {}).setdefault("libraries", {})["enabled"] = True
        else:
            rules.setdefault("sections", {}).setdefault("imports", {})["enabled"] = True

    return rules


def is_enabled(rules: Dict[str, Any], section_key: str) -> bool:
    try:
        return bool(rules.get("sections", {}).get(section_key, {}).get("enabled", True))
    except Exception:
        return True


def get_changelog_config(rules: Dict[str, Any]) -> Dict[str, Any]:
    """Возвращает конфиг changelog из правил."""
    cfg = rules.get("changelog") or {}
    return {
        "branches_only": cfg.get("branches_only", True),
        "task_key_pattern": cfg.get("task_key_pattern") or r"[A-Z][A-Z0-9]+-\d+",
        "branch_prefix_to_category": cfg.get("branch_prefix_to_category") or {
            "feature/": "Добавлено", "feat/": "Добавлено",
            "bugfix/": "Исправлено", "fix/": "Исправлено", "hotfix/": "Исправлено",
            "release/": "Изменено", "refactor/": "Изменено",
            "remove/": "Удалено", "revert/": "Удалено",
        },
        "task_tracker_url": cfg.get("task_tracker_url"),
    }

