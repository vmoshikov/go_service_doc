#!/usr/bin/env python3
"""
CHANGELOG Generator

Automatically generates and updates CHANGELOG.md based on git commits and code changes
using tree-sitter analysis and AI, following keepachangelog.com format.
"""

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from changelog.git_analyzer import GitAnalyzer
from rules import get_changelog_config, load_rules_for_repo, normalize_rules

KEEP_A_CHANGELOG_URL_RU = "https://keepachangelog.com/ru/0.3.0/"
SEMVER_URL = "https://semver.org/spec/v2.0.0.html"

CONVENTIONAL_RE = re.compile(
    r"^(?P<type>[a-zA-Z]+)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r"(?P<breaking>!)?: "
    r"(?P<description>.+)$"
)
BREAKING_FOOTER_RE = re.compile(r"^\s*BREAKING[\-\s]CHANGE:\s*(.+)\s*$", re.IGNORECASE | re.MULTILINE)

# Keep a Changelog sections (RU output, EN aliases accepted on parse)
KEEP_A_CHANGELOG_CATEGORIES_RU = ("Добавлено", "Изменено", "Устарело", "Удалено", "Исправлено", "Безопасность")
KEEP_A_CHANGELOG_CATEGORIES_EN = ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security")
KEEP_A_CHANGELOG_CATEGORY_ALIASES_TO_RU = {
    "added": "Добавлено",
    "changed": "Изменено",
    "deprecated": "Устарело",
    "removed": "Удалено",
    "fixed": "Исправлено",
    "security": "Безопасность",
    # RU lowercase fallback
    "добавлено": "Добавлено",
    "изменено": "Изменено",
    "устарело": "Устарело",
    "удалено": "Удалено",
    "исправлено": "Исправлено",
    "безопасность": "Безопасность",
}


@dataclass(frozen=True)
class CommitInfo:
    sha: str
    subject: str
    body: str
    author: str
    email: str
    date_iso: str


@dataclass(frozen=True)
class ParsedCommit:
    commit: CommitInfo
    conventional_type: Optional[str]
    conventional_scope: Optional[str]
    description: str
    is_breaking: bool
    jira_key: Optional[str]


class GigaChatClientStub:
    """
    Заглушка вместо реального GigaChat.

    Реальная интеграция должна:
    - принимать набор коммитов/дифф как "событие"
    - возвращать человекочитаемую строку для пункта CHANGELOG
    """

    def __init__(self, jira_base_url: Optional[str] = None):
        self.jira_base_url = jira_base_url.rstrip("/") if jira_base_url else None

    def summarize_event(self, *, category: str, jira_key: Optional[str], commits: List[ParsedCommit]) -> str:
        """
        Возвращает текст для bullet-пункта (без лидирующего "- ").
        """
        # Простая детерминированная эвристика вместо LLM:
        # - если группа по JIRA: используем ключ + краткое описание
        # - иначе: используем самое частое/первое описание
        if not commits:
            return "Небольшие изменения"

        descriptions = [c.description.strip() for c in commits if c.description.strip()]
        base = descriptions[0] if descriptions else commits[0].commit.subject.strip()

        if jira_key:
            jira_part = jira_key
            if self.jira_base_url:
                jira_part = f"[{jira_key}]({self.jira_base_url}/browse/{jira_key})"
            if len(commits) == 1:
                return f"{jira_part}: {base}"
            return f"{jira_part}: {base} (+{len(commits)-1} связанных коммит(ов))"

        # No JIRA key: de-duplicate by message.
        if len(commits) == 1:
            return base
        return f"{base} (+{len(commits)-1} связанных коммит(ов))"


class ChangelogGenerator:
    def __init__(
        self,
        go_dir: Path,
        output_path: Optional[Path] = None,
        rules: Optional[Dict] = None,
    ):
        self.go_dir = go_dir
        self.rules = rules or {}
        self._changelog_cfg = get_changelog_config(self.rules)
        self._task_key_re = re.compile(
            "(" + self._changelog_cfg["task_key_pattern"] + ")"
        )
        if output_path:
            out = output_path
            # If user passed a directory, write CHANGELOG.md inside it.
            if out.exists() and out.is_dir():
                out = out / "CHANGELOG.md"
            # Heuristic: if path has no suffix, treat it as directory.
            if (not out.suffix) and (not str(out).endswith(".md")):
                out = out / "CHANGELOG.md"
            self.changelog_path = out
        else:
            self.changelog_path = go_dir / "CHANGELOG.md"
        self.git_analyzer = GitAnalyzer(go_dir)
        tracker_url = self._changelog_cfg.get("task_tracker_url") or os.getenv("JIRA_BASE_URL")
        self.llm = GigaChatClientStub(jira_base_url=tracker_url)
    
    def generate(self, version: Optional[str] = None, since: Optional[str] = None):
        """
        Generate or update CHANGELOG.md.

        Primary mode (per requirements): when a new tag appears, generate a release
        section from the diff between previous tag and the new tag, and update
        CHANGELOG.md in Keep a Changelog format.
        """

        # 0) If changelog is created for the first time, generate full history.
        if self._is_first_time_changelog():
            print("CHANGELOG.md is missing or looks like a placeholder. Generating full changelog...")
            full = self._generate_full_changelog()
            self._write_changelog(full)
            print("CHANGELOG.md updated successfully!")
            return

        # 1) Resolve target tag/version
        tag, release_version = self._resolve_release_target(version)
        if not tag and version and release_version:
            # Manual release mode: create section for provided version from (since..HEAD] or (latest_tag..HEAD].
            content = self._load_or_init_changelog()
            if self._has_version_section(content, release_version):
                print(f"CHANGELOG already contains version [{release_version}]. Nothing to do.")
                return

            older_ref = since or self.git_analyzer.get_latest_tag()
            print(f"Manual release mode: {older_ref or '<root>'}..HEAD => [{release_version}]")
            commits = self.git_analyzer.get_commits_between(older_ref, "HEAD")
            if not commits:
                print("No commits found for release range. Nothing to update.")
                return
            diff_files = self.git_analyzer.get_diff_name_status(older_ref, "HEAD")
            release_date = datetime.now().strftime("%Y-%m-%d")
            entries_by_category = self._build_release_entries(
                commits=commits, diff_files=diff_files,
                older_ref=older_ref, newer_ref="HEAD",
            )
            new_content = self._insert_release_section(
                content=content,
                version=release_version,
                date=release_date,
                entries_by_category=entries_by_category,
                move_unreleased=True,
            )
            self._write_changelog(new_content)
            print("CHANGELOG.md updated successfully!")
            return

        if not tag:
            # Fallback (no tags): update Unreleased from recent commits.
            print("No git tags found. Updating [Unreleased] from recent commits...")
            commits = self.git_analyzer.get_commits_since(since)
            if not commits:
                print("No new commits found.")
                return
            content = self._load_or_init_changelog()
            updated = self._update_unreleased_from_commits(content, commits)
            self._write_changelog(updated)
            print("CHANGELOG.md updated successfully!")
            return

        # 2) Backfill any missing tag sections (older releases) without touching Unreleased.
        content = self._load_or_init_changelog()
        content = self._backfill_missing_tag_sections(content, skip_tag=tag)

        # 3) If target release already exists in CHANGELOG, we are done (after backfill).
        if self._has_version_section(content, release_version):
            print(f"CHANGELOG already contains version [{release_version}]. Nothing to do.")
            # Still persist backfilled content if it changed.
            self._write_changelog(content)
            return

        # 4) Determine range (previous tag by default, overridden by --since).
        older_ref = since or self.git_analyzer.get_previous_tag(tag)

        print(f"Analyzing release diff: {older_ref or '<root>'}..{tag}")
        commits = self.git_analyzer.get_commits_between(older_ref, tag)
        if self._changelog_cfg.get("branches_only"):
            merges = self.git_analyzer.get_merged_branches_in_range(older_ref, tag)
            if not merges:
                print("No merge commits (branches) found in release range. Nothing to update.")
                return
        elif not commits:
            print("No commits found for release range. Nothing to update.")
            return

        diff_files = self.git_analyzer.get_diff_name_status(older_ref, tag)
        release_date = self._get_ref_date(tag) or datetime.now().strftime("%Y-%m-%d")

        # 5) Build changelog bullets (по веткам: 1 ветка = 1 пункт, или по коммитам).
        entries_by_category = self._build_release_entries(
            commits=commits, diff_files=diff_files,
            older_ref=older_ref, newer_ref=tag,
        )

        # 6) Merge + roll Unreleased into the release (Keep a Changelog workflow).
        new_content = self._insert_release_section(
            content=content,
            version=release_version,
            date=release_date,
            entries_by_category=entries_by_category,
            move_unreleased=True,
        )

        self._write_changelog(new_content)
        print("CHANGELOG.md updated successfully!")

    def _backfill_missing_tag_sections(self, content: str, *, skip_tag: str) -> str:
        """
        Ensure CHANGELOG contains sections for all git tags.
        We backfill only tags *older* than skip_tag. The skip_tag is handled by the main flow
        so we can move Unreleased into it when it is new.
        """
        tags_newest_first = self.git_analyzer.get_tags_sorted()
        if not tags_newest_first:
            return content

        # Insert in chronological order (oldest -> newest) so newest ends up closest to Unreleased.
        tags_oldest_first = list(reversed(tags_newest_first))
        changed = False

        for tag in tags_oldest_first:
            if tag == skip_tag:
                continue
            version = tag.lstrip("v")
            if self._has_version_section(content, version):
                continue
            prev = self.git_analyzer.get_previous_tag(tag)
            commits = self.git_analyzer.get_commits_between(prev, tag)
            if not commits and not self._changelog_cfg.get("branches_only"):
                continue
            if self._changelog_cfg.get("branches_only"):
                merges = self.git_analyzer.get_merged_branches_in_range(prev, tag)
                if not merges:
                    continue
            date = self._get_ref_date(tag) or datetime.now().strftime("%Y-%m-%d")
            entries = self._build_release_entries(
                commits=commits, diff_files=self.git_analyzer.get_diff_name_status(prev, tag),
                older_ref=prev, newer_ref=tag,
            )
            content = self._insert_release_section(
                content=content,
                version=version,
                date=date,
                entries_by_category=entries,
                move_unreleased=False,
            )
            changed = True

        return content if changed else content

    def _is_first_time_changelog(self) -> bool:
        """
        Decide whether we should generate a full changelog.

        True when:
        - output file doesn't exist, OR
        - it doesn't contain Keep a Changelog sections (likely placeholder), OR
        - it has no release sections at all (no '## [x.y.z] - YYYY-MM-DD').
        """
        if not self.changelog_path.exists():
            return True
        try:
            raw = self.changelog_path.read_text(encoding="utf-8")
        except Exception:
            return True

        if not raw.strip():
            return True

        # Placeholder created by docs generator or other templates.
        if "Этот файл зарезервирован под changelog" in raw:
            return True

        # No Unreleased marker and no version-like sections -> not a real changelog yet.
        has_any_release = re.search(r"^## \[[^\]]+\]\s*-\s*\d{4}-\d{2}-\d{2}\s*$", raw, flags=re.MULTILINE) is not None
        has_unreleased = "## [Unreleased]" in raw
        if not has_unreleased and not has_any_release:
            return True

        # If there is Unreleased but no releases, treat as first run too.
        if has_unreleased and not has_any_release:
            return True

        return False

    def _generate_full_changelog(self) -> str:
        """
        Build a full Keep a Changelog file:
        - Header (RU)
        - Unreleased (commits since latest tag, if any)
        - Sections for all tags (newest first)
        """
        header = (
            "# Changelog\n\n"
            "Все заметные изменения этого проекта будут документироваться в этом файле.\n\n"
            f"Формат основан на [Keep a Changelog]({KEEP_A_CHANGELOG_URL_RU}),\n"
            f"и проект следует [Semantic Versioning]({SEMVER_URL}).\n\n"
        )

        tags_newest_first = self.git_analyzer.get_tags_sorted()
        latest_tag = tags_newest_first[0] if tags_newest_first else None

        # Unreleased: commits after latest tag (or entire history if no tags).
        unreleased_commits: List[Dict]
        if latest_tag:
            unreleased_commits = self.git_analyzer.get_commits_between(latest_tag, "HEAD")
        else:
            unreleased_commits = self.git_analyzer.get_commits_since(None)

        unreleased_entries = self._build_release_entries(
            commits=unreleased_commits, diff_files=[],
            older_ref=latest_tag, newer_ref="HEAD",
        )
        unreleased_section = self._render_release_section(version="Unreleased", date="", entries_by_category=unreleased_entries)

        parts: List[str] = [header.rstrip(), "", unreleased_section.rstrip(), ""]

        # Release sections: iterate oldest->newest while inserting after Unreleased is not needed here,
        # just append in newest-first order.
        for tag in tags_newest_first:
            prev = self.git_analyzer.get_previous_tag(tag)
            commits = self.git_analyzer.get_commits_between(prev, tag)
            if not commits and not self._changelog_cfg.get("branches_only"):
                continue
            if self._changelog_cfg.get("branches_only"):
                merges = self.git_analyzer.get_merged_branches_in_range(prev, tag)
                if not merges:
                    continue
            date = self._get_ref_date(tag) or datetime.now().strftime("%Y-%m-%d")
            entries = self._build_release_entries(
                commits=commits, diff_files=self.git_analyzer.get_diff_name_status(prev, tag),
                older_ref=prev, newer_ref=tag,
            )
            version = tag.lstrip("v")
            parts.append(self._render_release_section(version=version, date=date, entries_by_category=entries))
            parts.append("")

        return "\n".join(parts).rstrip() + "\n"
    
    def _resolve_release_target(self, version: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns (tag, release_version).

        - If `version` is provided, it may be "1.2.3" or "v1.2.3".
        - If not provided, uses latest git tag.
        """
        tags = self.git_analyzer.get_tags_sorted()
        if version:
            if version in tags:
                return version, version.lstrip("v")
            v = f"v{version}"
            if v in tags:
                return v, version
            # Not an existing tag: treat it as an explicit "version string" (manual mode).
            return None, version.lstrip("v")

        latest = self.git_analyzer.get_latest_tag()
        if not latest:
            return None, None
        return latest, latest.lstrip("v")

    def _get_ref_date(self, ref: str) -> Optional[str]:
        """Return short date (YYYY-MM-DD) for a git ref."""
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%ad", "--date=short", ref],
                cwd=self.go_dir,
                capture_output=True,
                text=True,
                check=True,
            )
            d = result.stdout.strip()
            return d or None
        except Exception:
            return None

    def _load_or_init_changelog(self) -> str:
        header = (
            "# Changelog\n\n"
            "Все заметные изменения этого проекта будут документироваться в этом файле.\n\n"
            f"Формат основан на [Keep a Changelog]({KEEP_A_CHANGELOG_URL_RU}),\n"
            f"и проект следует [Semantic Versioning]({SEMVER_URL}).\n\n"
            "## [Unreleased]\n\n"
        )

        if not self.changelog_path.exists():
            return header

        content = self.changelog_path.read_text(encoding="utf-8")
        if not content.strip():
            return header

        # Ensure header exists (do not destroy existing content).
        if not content.lstrip().startswith("# Changelog"):
            # If this looks like a placeholder, overwrite completely.
            if "Этот файл зарезервирован под changelog" in content or content.lstrip().startswith("# CHANGELOG"):
                return header
            content = header.rstrip() + "\n\n" + content.lstrip()

        # Ensure [Unreleased] section exists.
        if "## [Unreleased]" not in content:
            m_first_section = re.search(r"^## \[[^\]]+\]\s*$", content, flags=re.MULTILINE)
            insert_at = m_first_section.start() if m_first_section else len(content)
            content = content[:insert_at].rstrip() + "\n\n## [Unreleased]\n\n" + content[insert_at:].lstrip("\n")

        return content

    def _write_changelog(self, content: str) -> None:
        self.changelog_path.parent.mkdir(parents=True, exist_ok=True)
        self.changelog_path.write_text(content.rstrip() + "\n", encoding="utf-8")

    def _has_version_section(self, content: str, version: str) -> bool:
        return re.search(rf"^## \[{re.escape(version)}\]\b", content, flags=re.MULTILINE) is not None

    def _update_unreleased_from_commits(self, content: str, commits: List[Dict]) -> str:
        """
        Best-effort: build changelog bullets from commits and merge into [Unreleased].
        """
        entries_by_category = self._build_release_entries(commits=commits, diff_files=[])
        return self._insert_release_section(
            content=content,
            version="Unreleased",
            date="",
            entries_by_category=entries_by_category,
            move_unreleased=False,
            replace_unreleased=True,
        )

    def _build_release_entries(
        self,
        *,
        commits: List[Dict],
        diff_files: List[Tuple[str, str]],
        older_ref: Optional[str] = None,
        newer_ref: Optional[str] = None,
    ) -> Dict[str, List[str]]:
        """
        Строит пункты changelog. Если branches_only — только по merge-веткам (1 ветка = 1 пункт).
        Иначе — по коммитам (группировка по задаче/сообщению).
        """
        if self._changelog_cfg.get("branches_only") and older_ref is not None and newer_ref is not None:
            return self._build_release_entries_from_branches(older_ref=older_ref, newer_ref=newer_ref)
        return self._build_release_entries_from_commits(commits=commits, diff_files=diff_files)

    def _build_release_entries_from_branches(
        self, *, older_ref: str, newer_ref: str
    ) -> Dict[str, List[str]]:
        """
        1 ветка = 1 задача = 1 пункт. Только merge-коммиты в теге.
        """
        merges = self.git_analyzer.get_merged_branches_in_range(older_ref, newer_ref)
        prefix_map = self._changelog_cfg.get("branch_prefix_to_category") or {}

        entries_by_category: Dict[str, List[str]] = {k: [] for k in KEEP_A_CHANGELOG_CATEGORIES_RU}

        for m in merges:
            branch_name = m.get("branch_name")
            if not branch_name:
                continue
            task_key = None
            mo = self._task_key_re.search(branch_name)
            if mo:
                task_key = mo.group(1)

            category = "Изменено"
            branch_lower = branch_name.lower()
            for prefix, cat in prefix_map.items():
                if branch_lower.startswith(prefix.lower()):
                    category = cat
                    break

            if category not in entries_by_category:
                entries_by_category[category] = []

            desc = self._branch_to_description(branch_name, m.get("subject", ""), task_key)
            bullet = self.llm.summarize_event(
                category=category,
                jira_key=task_key,
                commits=[ParsedCommit(
                    commit=CommitInfo(sha=m["hash"], subject=m["subject"], body=m.get("body", ""),
                                    author="", email="", date_iso=""),
                    conventional_type=None,
                    conventional_scope=None,
                    description=desc,
                    is_breaking=False,
                    jira_key=task_key,
                )],
            )
            bullet = bullet.strip().lstrip("-").strip()
            if bullet:
                entries_by_category[category].append(bullet)

        for k in list(entries_by_category.keys()):
            seen = set()
            entries_by_category[k] = [b for b in entries_by_category[k] if b not in seen and not seen.add(b)]

        return entries_by_category

    def _branch_to_description(self, branch_name: str, merge_subject: str, task_key: Optional[str]) -> str:
        """Краткое описание из имени ветки (часть после task_key) или из merge subject."""
        if task_key and task_key in branch_name:
            rest = branch_name.split(task_key, 1)[-1].strip("-_/ ")
            if rest:
                return rest.replace("-", " ").replace("_", " ")
        if merge_subject:
            for prefix in ("Merge branch ", "Merge ", "Merge pull "):
                if merge_subject.startswith(prefix):
                    return merge_subject[len(prefix):].strip("'\"").split("'")[0] or branch_name
        return branch_name

    def _build_release_entries_from_commits(
        self, *, commits: List[Dict], diff_files: List[Tuple[str, str]]
    ) -> Dict[str, List[str]]:
        """Fallback: группировка по коммитам (задача/сообщение)."""
        parsed: List[ParsedCommit] = []
        for c in commits:
            ci = CommitInfo(
                sha=c.get("hash", ""),
                subject=c.get("subject", "") or "",
                body=c.get("body", "") or "",
                author=c.get("author", "") or "",
                email=c.get("email", "") or "",
                date_iso=c.get("date", "") or "",
            )
            parsed.append(self._parse_commit(ci))

        groups: Dict[str, List[ParsedCommit]] = {}
        for pc in parsed:
            key = pc.jira_key or self._normalize_group_message(pc.description or pc.commit.subject)
            groups.setdefault(key, []).append(pc)

        entries_by_category: Dict[str, List[str]] = {k: [] for k in KEEP_A_CHANGELOG_CATEGORIES_RU}

        for group_key, pcs in groups.items():
            category = self._choose_category_for_group(pcs)
            if not category:
                continue
            jira_key = pcs[0].jira_key if pcs and pcs[0].jira_key else None
            bullet = self.llm.summarize_event(category=category, jira_key=jira_key, commits=pcs)
            bullet = bullet.strip().lstrip("-").strip()
            if not bullet:
                continue
            entries_by_category[category].append(bullet)

        for k in list(entries_by_category.keys()):
            seen = set()
            entries_by_category[k] = [b for b in entries_by_category[k] if b not in seen and not seen.add(b)]

        return entries_by_category

    def _parse_commit(self, commit: CommitInfo) -> ParsedCommit:
        subject = commit.subject.strip()
        body = commit.body or ""
        full_text = f"{subject}\n{body}"

        jira_key = None
        mo = self._task_key_re.search(full_text)
        if mo:
            jira_key = mo.group(1)

        conventional_type = None
        conventional_scope = None
        description = subject
        is_breaking = False

        m = CONVENTIONAL_RE.match(subject)
        if m:
            conventional_type = (m.group("type") or "").lower()
            conventional_scope = m.group("scope")
            description = (m.group("description") or "").strip() or subject
            is_breaking = bool(m.group("breaking"))

        if BREAKING_FOOTER_RE.search(body):
            is_breaking = True

        return ParsedCommit(
            commit=commit,
            conventional_type=conventional_type,
            conventional_scope=conventional_scope,
            description=description,
            is_breaking=is_breaking,
            jira_key=jira_key,
        )

    def _normalize_group_message(self, msg: str) -> str:
        msg = (msg or "").strip()
        msg = re.sub(r"\s+", " ", msg)
        return msg.lower()

    def _choose_category_for_group(self, commits: List[ParsedCommit]) -> Optional[str]:
        """
        Choose a single Keep a Changelog category for a group.
        Приоритет: Безопасность > Удалено > Устарело > Исправлено > Добавлено > Изменено
        """
        if not commits:
            return None

        texts = " ".join([(c.commit.subject or "") + " " + (c.commit.body or "") for c in commits]).lower()
        if any(w in texts for w in ["security", "vulnerability", "cve", "exploit"]):
            return "Безопасность"

        # Based on conventional commit types, best-effort.
        type_map = {
            "feat": "Добавлено",
            "fix": "Исправлено",
            "perf": "Изменено",
            "refactor": "Изменено",
            "docs": "Изменено",
            "chore": "Изменено",
            "build": "Изменено",
            "ci": "Изменено",
            "test": "Изменено",
            "style": "Изменено",
            "revert": "Исправлено",
        }

        categories = []
        for c in commits:
            ct = (c.conventional_type or "").lower() if c.conventional_type else ""
            categories.append(type_map.get(ct, "Изменено"))

        priority = {"Безопасность": 0, "Удалено": 1, "Устарело": 2, "Исправлено": 3, "Добавлено": 4, "Изменено": 5}
        chosen = sorted(categories, key=lambda x: priority.get(x, 99))[0] if categories else "Изменено"

        # Filter out pure maintenance noise unless tied to a task/breaking change.
        noisy_types = {"chore", "build", "ci", "test", "style"}
        if all((c.conventional_type or "") in noisy_types for c in commits):
            if not any(c.jira_key for c in commits) and not any(c.is_breaking for c in commits):
                return None

        return chosen

    def _render_release_section(self, *, version: str, date: str, entries_by_category: Dict[str, List[str]]) -> str:
        lines: List[str] = []
        if version == "Unreleased":
            lines.append("## [Unreleased]")
            lines.append("")
        else:
            lines.append(f"## [{version}] - {date}")
            lines.append("")

        for cat in KEEP_A_CHANGELOG_CATEGORIES_RU:
            items = entries_by_category.get(cat) or []
            if not items:
                continue
            lines.append(f"### {cat}")
            for it in items:
                lines.append(f"- {it}")
            lines.append("")

        return "\n".join(lines).rstrip()

    def _extract_unreleased_entries(self, content: str) -> Tuple[Dict[str, List[str]], str]:
        """
        Extract and remove entries from the [Unreleased] section.
        Returns (entries_by_category, remaining_content_with_empty_unreleased).
        """
        m = re.search(r"^## \[Unreleased\]\s*$", content, flags=re.MULTILINE)
        if not m:
            return {k: [] for k in KEEP_A_CHANGELOG_CATEGORIES_RU}, content

        header_line_end = content.find("\n", m.end())
        if header_line_end == -1:
            header_line_end = len(content)
        header_end = header_line_end + 1 if header_line_end < len(content) else len(content)

        m_next = re.search(r"^## \[[^\]]+\]\s*$", content[header_end:], flags=re.MULTILINE)
        section_end = header_end + (m_next.start() if m_next else len(content) - header_end)

        block = content[header_end:section_end]
        entries = {k: [] for k in KEEP_A_CHANGELOG_CATEGORIES_RU}

        current_cat: Optional[str] = None
        for line in block.splitlines():
            line = line.rstrip()
            if line.startswith("### "):
                name = line.replace("### ", "", 1).strip()
                key = name.strip()
                # Accept both RU and EN headings
                if key in KEEP_A_CHANGELOG_CATEGORIES_RU:
                    current_cat = key
                elif key in KEEP_A_CHANGELOG_CATEGORIES_EN:
                    current_cat = KEEP_A_CHANGELOG_CATEGORY_ALIASES_TO_RU.get(key.lower())
                else:
                    current_cat = KEEP_A_CHANGELOG_CATEGORY_ALIASES_TO_RU.get(key.lower())
                continue
            if current_cat and line.startswith("- "):
                entries[current_cat].append(line[2:].strip())

        # Remove original unreleased body; keep header + blank line.
        cleaned = content[:header_end] + "\n" + content[section_end:].lstrip("\n")
        return entries, cleaned

    def _insert_release_section(
        self,
        *,
        content: str,
        version: str,
        date: str,
        entries_by_category: Dict[str, List[str]],
        move_unreleased: bool,
        replace_unreleased: bool = False,
    ) -> str:
        """
        Insert a release section right after [Unreleased]. Optionally move bullets
        from [Unreleased] into the generated release section.

        If replace_unreleased=True, overwrites [Unreleased] section with the rendered one.
        """
        content = content if content.endswith("\n") else content + "\n"

        if "## [Unreleased]" not in content:
            # Ensure skeleton exists.
            content = self._load_or_init_changelog() + content.lstrip()

        unreleased_entries = {k: [] for k in KEEP_A_CHANGELOG_CATEGORIES_RU}
        if move_unreleased:
            unreleased_entries, content = self._extract_unreleased_entries(content)

        merged = {k: list(entries_by_category.get(k) or []) for k in KEEP_A_CHANGELOG_CATEGORIES_RU}
        for cat in KEEP_A_CHANGELOG_CATEGORIES_RU:
            merged[cat].extend(unreleased_entries.get(cat) or [])
            # de-dup
            seen = set()
            out = []
            for b in merged[cat]:
                if b in seen:
                    continue
                seen.add(b)
                out.append(b)
            merged[cat] = out

        if replace_unreleased and version == "Unreleased":
            # Replace only Unreleased block with freshly rendered content.
            m = re.search(r"^## \[Unreleased\]\s*$", content, flags=re.MULTILINE)
            if not m:
                return content
            header_line_end = content.find("\n", m.end())
            if header_line_end == -1:
                header_line_end = len(content)
            header_end = header_line_end + 1 if header_line_end < len(content) else len(content)
            m_next = re.search(r"^## \[[^\]]+\]\s*$", content[header_end:], flags=re.MULTILINE)
            section_end = header_end + (m_next.start() if m_next else len(content) - header_end)
            rendered = self._render_release_section(version="Unreleased", date="", entries_by_category=merged)
            return (content[: m.start()] + rendered + "\n\n" + content[section_end:].lstrip("\n")).rstrip() + "\n"

        release_section = self._render_release_section(version=version, date=date, entries_by_category=merged)

        # Insert after Unreleased header line (keeping Unreleased empty if move_unreleased=True).
        m = re.search(r"^## \[Unreleased\]\s*$", content, flags=re.MULTILINE)
        if not m:
            return content.rstrip() + "\n\n" + release_section + "\n"

        header_line_end = content.find("\n", m.end())
        if header_line_end == -1:
            header_line_end = len(content)
        header_end = header_line_end + 1 if header_line_end < len(content) else len(content)

        # If we moved unreleased, ensure it's empty (single blank line after header).
        if move_unreleased:
            # Remove any remaining body under Unreleased if present.
            m_next = re.search(r"^## \[[^\]]+\]\s*$", content[header_end:], flags=re.MULTILINE)
            section_end = header_end + (m_next.start() if m_next else len(content) - header_end)
            content = content[:header_end] + "\n" + content[section_end:].lstrip("\n")

        insertion_point = header_end
        return (content[:insertion_point] + "\n" + release_section + "\n\n" + content[insertion_point:].lstrip("\n")).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Generate/update CHANGELOG.md from git tags and commits (Keep a Changelog)"
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Path to the Go service directory'
    )
    parser.add_argument(
        '--version',
        type=str,
        help='Release version/tag to generate (e.g., 1.0.0 or v1.0.0). If not provided, uses latest tag'
    )
    parser.add_argument(
        '--since',
        type=str,
        help='Lower bound ref for release diff (default: previous tag). Examples: v1.0.0, HEAD~10'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output path for CHANGELOG.md (file or directory). Default: <repo>/CHANGELOG.md'
    )
    parser.add_argument(
        '--task-pattern',
        type=str,
        default=None,
        help='Regex для ключа задачи (ключ-число). Переопределяет rules/changelog.task_key_pattern'
    )
    
    args = parser.parse_args()
    
    go_dir = Path(args.directory).expanduser().resolve()
    if not go_dir.exists():
        print(f"Error: Directory '{go_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    repo_name = go_dir.name
    rules, _ = load_rules_for_repo(repo_name, Path.cwd())
    if not _:
        rules, _ = load_rules_for_repo(repo_name, Path(__file__).resolve().parent)
    rules = normalize_rules(rules)
    if args.task_pattern:
        rules.setdefault("changelog", {})["task_key_pattern"] = args.task_pattern
    
    output_path = Path(args.output).expanduser().resolve() if args.output else None
    generator = ChangelogGenerator(go_dir, output_path=output_path, rules=rules)
    generator.generate(version=args.version, since=args.since)


if __name__ == '__main__':
    main()
