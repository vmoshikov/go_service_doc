#!/usr/bin/env python3
"""
Go Service Documentation Generator

A service that generates comprehensive documentation for Go services by analyzing
the codebase and combining user-provided sections with auto-generated content.
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from parsers.function_parser import FunctionParser
from parsers.api_parser import APIParser
from parsers.test_parser import TestParser
from parsers.library_parser import LibraryParser
from parsers.import_parser import ImportParser
from parsers.struct_parser import StructParser
from generators.doc_generator import DocumentationGenerator
from rules import (
    load_rules_for_repo,
    normalize_rules,
    is_enabled,
    is_function_test_registry_enabled,
    is_er_diagram_enabled,
)
from changelog_generator import ChangelogGenerator


def _update_docs_index(docs_root: Path) -> None:
    """Обновить docs/_index.md со списком всех проектов для Hugo."""
    if not docs_root.exists():
        return
    projects: List[str] = []
    for item in sorted(docs_root.iterdir()):
        if not item.is_dir() or item.name.startswith('.'):
            continue
        # Проект: есть README, sections или CHANGELOG
        if (
            (item / "README.md").exists()
            or (item / "sections").is_dir()
            or (item / "CHANGELOG.md").exists()
        ):
            projects.append(item.name)
    if not projects:
        return
    index_path = docs_root / "_index.md"
    lines = [
        "---",
        'title: "Документация Go сервисов"',
        "---",
        "",
        "# Документация Go сервисов",
        "",
        "Автогенерируемая документация для Go сервисов. Выберите проект в меню слева.",
        "",
        "## Проекты",
        "",
    ]
    for name in projects:
        # Ссылка на README проекта, если есть; иначе — на раздел
        href = f"/{name}/readme/" if (docs_root / name / "README.md").exists() else f"/{name}/"
        lines.append(f"- [{name}]({href}) — документация сервиса {name}")
    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated docs index: {index_path}")


def _derive_repo_name(source: str) -> str:
    # URL: https://host/group/repo.git -> repo
    # SSH: git@host:group/repo.git -> repo
    s = source.strip().rstrip('/')
    if s.endswith('.git'):
        s = s[:-4]
    # take last path segment (after / or :)
    if '/' in s:
        s = s.split('/')[-1]
    if ':' in s:
        s = s.split(':')[-1]
        if '/' in s:
            s = s.split('/')[-1]
    return s or "repo"


def _resolve_source_from_env() -> Tuple[Optional[str], Optional[str]]:
    """
    Best-effort extraction of repository URL + ref from CI environments.
    - GitLab: CI_REPOSITORY_URL / CI_COMMIT_TAG / CI_COMMIT_REF_NAME
    - Generic: PROJECT_REPO_URL / GIT_URL / GIT_REF
    """
    repo_url = (
        os.environ.get("CI_REPOSITORY_URL")
        or os.environ.get("PROJECT_REPO_URL")
        or os.environ.get("GIT_URL")
    )
    ref = (
        os.environ.get("CI_COMMIT_TAG")
        or os.environ.get("CI_COMMIT_REF_NAME")
        or os.environ.get("GIT_REF")
    )
    return repo_url, ref


def _derive_web_url_from_repo_url(repo_url: str) -> Optional[str]:
    """
    Convert common git clone URLs into a web URL.
    Examples:
    - https://gitlab.com/group/repo.git -> https://gitlab.com/group/repo
    - git@gitlab.com:group/repo.git -> https://gitlab.com/group/repo
    - ssh://git@gitlab.com/group/repo.git -> https://gitlab.com/group/repo
    """
    if not repo_url:
        return None

    s = repo_url.strip()

    # ssh://git@host/group/repo(.git)
    if s.startswith("ssh://"):
        s2 = s[len("ssh://") :]
        # remove user@
        if "@" in s2:
            s2 = s2.split("@", 1)[1]
        # host/path
        if "/" in s2:
            host, path = s2.split("/", 1)
            path = path.rstrip("/")
            if path.endswith(".git"):
                path = path[:-4]
            return f"https://{host}/{path}"
        return None

    # git@host:group/repo(.git)
    if s.startswith("git@") and ":" in s:
        user_host, path = s.split(":", 1)
        host = user_host.split("@", 1)[1]
        path = path.rstrip("/")
        if path.endswith(".git"):
            path = path[:-4]
        return f"https://{host}/{path}"

    # https://host/group/repo(.git) or http://...
    if s.startswith("https://") or s.startswith("http://"):
        # strip credentials if any (http(s)://user:pass@host/..)
        proto, rest = s.split("://", 1)
        if "@" in rest and rest.split("@", 1)[0].count(":") >= 1:
            rest = rest.split("@", 1)[1]
        rest = rest.rstrip("/")
        if rest.endswith(".git"):
            rest = rest[:-4]
        return f"{proto}://{rest}"

    return None


def _clone_repo_to_temp(
    repo_url: str,
    ref: Optional[str],
    repo_name: str,
    *,
    shallow: bool = False,
) -> Path:
    """
    Clone repository into a temp directory.
    If ref is set: prefer `git clone --branch <ref> --single-branch`, then fallback to
    default clone + `git checkout <ref>` (needed for some tags/SHAs).
    """
    tmp_root = Path(tempfile.mkdtemp(prefix="go_service_doc_"))
    target_dir = tmp_root / repo_name

    depth_args = ["--depth", "1"] if shallow else []

    def clone_default() -> None:
        cmd = ["git", "clone", "--quiet", *depth_args, repo_url, str(target_dir)]
        subprocess.run(cmd, check=True)

    if not ref:
        clone_default()
        return target_dir

    # Try: clone directly on branch/tag (works for many branch names and some tags)
    cmd_branch = [
        "git",
        "clone",
        "--quiet",
        *depth_args,
        "--branch",
        ref,
        "--single-branch",
        repo_url,
        str(target_dir),
    ]
    result = subprocess.run(cmd_branch, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Cloned repository at ref: {ref}")
        return target_dir

    err_hint = (result.stderr or result.stdout or "").strip()
    if err_hint:
        print(f"Note: git clone --branch {ref!r} failed ({err_hint[:200]}); trying default clone + checkout.")

    if target_dir.exists():
        shutil.rmtree(target_dir)

    clone_default()
    co = subprocess.run(
        ["git", "-C", str(target_dir), "checkout", "--quiet", ref],
        capture_output=True,
        text=True,
    )
    if co.returncode != 0 and shallow:
        # Shallow clone may not include the requested commit
        print(f"Note: checkout {ref!r} failed with shallow clone; retrying full clone + checkout.")
        shutil.rmtree(target_dir)
        subprocess.run(["git", "clone", "--quiet", repo_url, str(target_dir)], check=True)
        subprocess.run(["git", "-C", str(target_dir), "checkout", "--quiet", ref], check=True)
    elif co.returncode != 0:
        subprocess.run(["git", "-C", str(target_dir), "checkout", "--quiet", ref], check=True)
    else:
        print(f"Checked out ref: {ref}")

    return target_dir


def _is_git_tag(repo_dir: Path, ref: str) -> bool:
    """Return True if `ref` exists as a tag in repo_dir."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_dir), "rev-parse", "-q", "--verify", f"refs/tags/{ref}"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate documentation for Go service from codebase'
    )
    parser.add_argument(
        'source',
        type=str,
        nargs='?',
        help='Path to Go service directory OR repository URL to clone'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='README.md',
        help='Output file name inside docs/<repo_name>/ (default: README.md)'
    )
    parser.add_argument(
        '--docs-root',
        type=str,
        default=None,
        help='Docs root directory (default: <cwd>/docs)'
    )
    parser.add_argument(
        '--repo-name',
        type=str,
        default=None,
        help='Repository name used for docs/<repo_name> (default: derived from source)'
    )
    parser.add_argument(
        '--ref',
        '--branch',
        type=str,
        default=None,
        dest='ref',
        metavar='REF',
        help=(
            'Branch, tag, or commit to use when cloning a remote repository '
            '(git clone --branch when possible, else checkout). Synonym: --branch. '
            'Default: CI_COMMIT_TAG / CI_COMMIT_REF_NAME / GIT_REF.'
        ),
    )
    parser.add_argument(
        '--shallow',
        action='store_true',
        help='Use git clone --depth 1 (faster; may fail for arbitrary SHAs — full clone is retried).',
    )
    parser.add_argument(
        '--repo-web-url',
        type=str,
        default=None,
        help='Optional web URL for source links (e.g. GitLab/GitHub project URL)'
    )
    parser.add_argument(
        '--proto-config',
        type=str,
        default=None,
        help='Path to proto config (e.g. docs/<repo_name>/proto_conf.json). If not set, auto-detected.'
    )
    parser.add_argument(
        '--no-changelog',
        action='store_true',
        help='Do not generate docs/<repo>/CHANGELOG.md'
    )
    parser.add_argument(
        '--changelog-only',
        action='store_true',
        help='Only generate docs/<repo>/CHANGELOG.md (skip README/sections generation)'
    )
    
    args = parser.parse_args()

    # Resolve source/ref from args or CI env
    env_repo_url, env_ref = _resolve_source_from_env()
    source = args.source or env_repo_url
    if not source:
        print("Error: source is required (local path or repo URL).", file=sys.stderr)
        print("Tip: Provide it as positional arg, or set CI_REPOSITORY_URL/PROJECT_REPO_URL.", file=sys.stderr)
        sys.exit(1)

    ref = args.ref if args.ref is not None else env_ref
    repo_name = args.repo_name or _derive_repo_name(source)

    # Determine docs root and per-repo docs directory
    docs_root = Path(args.docs_root).expanduser().resolve() if args.docs_root else (Path.cwd() / "docs")
    docs_dir = docs_root / repo_name
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Determine go_dir:
    # - if local path exists -> use it directly (test mode)
    # - else treat as repo URL and clone to temp
    source_path = Path(source)
    cloned_repo_dir: Optional[Path] = None
    if source_path.exists() and source_path.is_dir():
        go_dir = source_path.resolve()
    else:
        print(f"Cloning repository into a temporary directory: {source}")
        try:
            cloned_repo_dir = _clone_repo_to_temp(
                source, ref=ref, repo_name=repo_name, shallow=args.shallow
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: git clone failed: {e}", file=sys.stderr)
            sys.exit(1)
        go_dir = cloned_repo_dir

    print(f"Analyzing Go service at: {go_dir}")

    # User documentation directory: <go_repo>/docs/ (in source repository)
    user_docs_dir = go_dir / "docs"
    if not user_docs_dir.exists():
        user_docs_dir = None
        print(f"Tip: Create {go_dir.name}/docs/ directory in source repository for user-provided documentation")
    else:
        print(f"Found user documentation directory: {user_docs_dir}")

    # Load rules (priority order):
    # 1) docs/<repo_name>/RULES.md (in docs repository - user can customize before first generation)
    # 2) ./rules/<repo_name>.json (repo-specific override in generator repo)
    # 3) defaults
    rules = None
    rules_src = None
    
    # First: check docs/<repo_name>/RULES.md (highest priority - user customization)
    docs_rules_md = docs_dir / "RULES.md"
    if docs_rules_md.exists():
        from rules import load_rules_from_md
        rules = load_rules_from_md(docs_rules_md)
        rules_src = docs_rules_md
        print(f"Loaded rules from: {docs_rules_md}")
    
    # Second: check ./rules/<repo_name>.json
    if rules is None:
        rules, rules_src = load_rules_for_repo(repo_name, Path.cwd())
        if rules_src is None:
            rules2, rules_src2 = load_rules_for_repo(repo_name, Path(__file__).resolve().parent)
            if rules_src2 is not None:
                rules = rules2
                rules_src = rules_src2
    
    if rules_src:
        print(f"Using rules from: {rules_src}")
    else:
        print("Using default rules")
    
    rules = normalize_rules(rules)

    # External proto config (generator setting, stored in docs/<repo_name>/)
    proto_config_path: Optional[Path] = None
    if args.proto_config:
        proto_config_path = Path(args.proto_config).expanduser().resolve()
    else:
        candidates = [
            docs_dir / "proto_conf.json",
            docs_dir / ".doc_config.json",
            go_dir / ".doc_config.json",  # legacy
        ]
        for c in candidates:
            if c.exists():
                proto_config_path = c
                break

    if not proto_config_path:
        print("Tip: Create proto config to link external proto repositories:")
        print(f"     {docs_dir / 'proto_conf.json'}")
        print("     See EXTERNAL_PROTO.md for details")

    # Exclusion dirs: load from docs/<repo_name>/exclude.json, else from rules
    exclude_dirs: List[str] = []
    exclude_json_path = docs_dir / "exclude.json"
    if exclude_json_path.exists():
        try:
            exclude_cfg = json.loads(exclude_json_path.read_text(encoding="utf-8"))
            exclude_dirs = exclude_cfg.get("exclude_dirs") or []
        except Exception as e:
            print(f"Warning: Could not load exclude.json: {e}")
    if not exclude_dirs:
        exclude_dirs = rules.get("exclude_dirs") or []

    # Initialize parsers
    if (not args.no_changelog) and args.changelog_only:
        # Generate changelog into docs/<repo>/CHANGELOG.md and exit.
        tag_ref = None
        if ref and _is_git_tag(go_dir, ref):
            tag_ref = ref
        changelog_out = docs_dir / "CHANGELOG.md"
        print(f"Generating CHANGELOG: {changelog_out}")
        ChangelogGenerator(go_dir, output_path=changelog_out, rules=rules).generate(version=tag_ref)
        print(f"CHANGELOG generated successfully: {changelog_out}")
        _update_docs_index(docs_root)
        return

    cache_dir = docs_dir / ".cache"

    if proto_config_path and proto_config_path.exists():
        try:
            proto_cfg = json.loads(proto_config_path.read_text(encoding="utf-8"))
            ext = proto_cfg.get("external_repositories") or {}
            if ext:
                from parsers.proto_prefetch import prefetch_external_proto_repos

                prefetch_external_proto_repos(
                    cache_dir / "proto",
                    ext,
                    shallow=args.shallow,
                )
        except Exception as e:
            print(f"Warning: proto prefetch failed: {e}")

    function_parser = FunctionParser(go_dir, exclude_dirs=exclude_dirs)
    api_parser = APIParser(
        go_dir,
        config_path=proto_config_path,
        repo_name=repo_name,
        cache_dir=(cache_dir / "proto"),
        exclude_dirs=exclude_dirs,
    ) if is_enabled(rules, "api") else None
    want_test_parse = is_enabled(rules, "tests") or is_function_test_registry_enabled(rules)
    test_parser = TestParser(go_dir, exclude_dirs=exclude_dirs) if want_test_parse else None
    library_parser = LibraryParser(go_dir) if is_enabled(rules, "libraries") else None
    import_parser = ImportParser(
        go_dir,
        rules=rules,
        cache_dir=(cache_dir / "imports"),
        exclude_dirs=exclude_dirs,
    ) if is_enabled(rules, "imports") else None
    struct_parser = StructParser(go_dir, exclude_dirs=exclude_dirs) if is_enabled(rules, "structures") else None
    
    # Parse codebase
    api_spec: Dict = {"grpc": [], "rest": [], "structs": {}}
    if api_parser:
        print("Parsing API endpoints and structs...")
        api_spec = api_parser.parse()

    # If API parsing is disabled, but we still need structs (structures/functions),
    # parse structs separately.
    if (not api_parser) and struct_parser:
        print("Parsing structs...")
        api_spec["structs"] = struct_parser.parse()
    
    # Enrich structs from proto repository if available
    if proto_config_path and proto_config_path.exists():
        from parsers.proto_struct_extractor import ProtoStructExtractor
        from config import Config
        proto_config = Config(go_dir, config_path=proto_config_path, repo_name=repo_name)
        proto_extractor = ProtoStructExtractor(proto_config, cache_dir=(cache_dir / "proto"))
        proto_structs = proto_extractor.get_structs_for_project(repo_name)
        if proto_structs:
            print(f"Found {len(proto_structs)} structs from proto repository")
            # Get first external repo for source links (web URL + branch)
            source_repo_url = None
            source_branch = "main"
            for repo_info in (proto_config.external_repos or {}).values():
                if isinstance(repo_info, dict):
                    source_repo_url = repo_info.get("url") or source_repo_url
                    source_branch = repo_info.get("branch") or source_branch
                    if source_repo_url:
                        break
            if source_repo_url and source_repo_url.endswith(".git"):
                source_repo_url = source_repo_url[:-4]
            # Merge proto structs (proto takes precedence)
            for struct_name, struct_def in proto_structs.items():
                struct_def["from_proto"] = True
                if source_repo_url:
                    struct_def["source_repo_url"] = source_repo_url
                struct_def["source_branch"] = source_branch
                api_spec["structs"][struct_name] = struct_def
    
    # Pass structs to function parser for struct type extraction
    functions: List[Dict] = []
    if is_enabled(rules, "functions"):
        print("Parsing functions...")
        function_parser.set_structs(api_spec.get("structs", {}))
        functions = function_parser.parse()
    
    tests: Dict = {"tests": [], "benchmarks": [], "examples": []}
    if test_parser:
        print("Parsing tests...")
        tests = test_parser.parse()
    
    libraries: Dict = {"module": "unknown", "dependencies": [], "replace": []}
    if library_parser:
        print("Parsing libraries...")
        libraries = library_parser.parse()

    imports: Dict = {"module": "unknown", "imports": []}
    if import_parser:
        print("Parsing imports...")
        imports = import_parser.parse()
    
    migration_tables = None
    if is_er_diagram_enabled(rules):
        from parsers.migration_schema import build_schema_from_migrations

        migration_tables, mig_warn = build_schema_from_migrations(go_dir, rules)
        for w in mig_warn:
            print(f"Migration ER: {w}")

    # Generate documentation
    print("Generating documentation...")
    # Prefer explicit repo web URL, then CI_PROJECT_URL (if it actually points to source repo),
    # then derive from the clone URL (CI_REPOSITORY_URL/PROJECT_REPO_URL/arg source).
    repo_web_url = (
        args.repo_web_url
        or os.environ.get("SOURCE_REPO_WEB_URL")
        or os.environ.get("CI_PROJECT_URL")
        or _derive_web_url_from_repo_url(source)
        or _derive_web_url_from_repo_url(env_repo_url or "")
    )
    doc_generator = DocumentationGenerator(
        go_dir=go_dir,
        docs_dir=docs_dir,
        user_docs_dir=user_docs_dir,  # <go_repo>/docs/ from source repository
        repo_name=repo_name,
        repo_ref=ref,
        repo_web_url=repo_web_url,
        rules=rules,
    )
    doc_generator.set_structs(api_spec.get('structs', {}))
    doc_generator.generate(
        functions=functions,
        api_spec=api_spec,
        tests=tests,
        libraries=libraries,
        imports=imports,
        output_file=args.output,
        migration_tables=migration_tables,
    )
    
    print(f"Documentation generated successfully: {docs_dir / args.output}")

    # Generate changelog (default behavior)
    if not args.no_changelog:
        tag_ref = None
        if ref and _is_git_tag(go_dir, ref):
            tag_ref = ref
        changelog_out = docs_dir / "CHANGELOG.md"
        print(f"Generating CHANGELOG: {changelog_out}")
        ChangelogGenerator(go_dir, output_path=changelog_out, rules=rules).generate(version=tag_ref)
        print(f"CHANGELOG generated successfully: {changelog_out}")

    _update_docs_index(docs_root)


if __name__ == '__main__':
    main()
