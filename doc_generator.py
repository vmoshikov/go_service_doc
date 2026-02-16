#!/usr/bin/env python3
"""
Go Service Documentation Generator

A service that generates comprehensive documentation for Go services by analyzing
the codebase and combining user-provided sections with auto-generated content.
"""

import argparse
import os
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
from rules import load_rules_for_repo, normalize_rules, is_enabled
from changelog_generator import ChangelogGenerator


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


def _clone_repo_to_temp(repo_url: str, ref: Optional[str], repo_name: str) -> Path:
    tmp_root = Path(tempfile.mkdtemp(prefix="go_service_doc_"))
    target_dir = tmp_root / repo_name

    clone_cmd = ["git", "clone", "--quiet", repo_url, str(target_dir)]
    subprocess.run(clone_cmd, check=True)

    if ref:
        # Try checkout ref (tag/branch/commit)
        subprocess.run(["git", "-C", str(target_dir), "checkout", "--quiet", ref], check=False)

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
        type=str,
        default=None,
        help='Tag/branch/commit to checkout after cloning (default: from CI env)'
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

    ref = args.ref or env_ref
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
            cloned_repo_dir = _clone_repo_to_temp(source, ref=ref, repo_name=repo_name)
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
        return

    function_parser = FunctionParser(go_dir)
    cache_dir = docs_dir / ".cache"
    api_parser = APIParser(
        go_dir, 
        config_path=proto_config_path,
        repo_name=repo_name,
        cache_dir=(cache_dir / "proto")
    ) if is_enabled(rules, "api") else None
    test_parser = TestParser(go_dir) if is_enabled(rules, "tests") else None
    library_parser = LibraryParser(go_dir) if is_enabled(rules, "libraries") else None
    import_parser = ImportParser(
        go_dir,
        rules=rules,
        cache_dir=(cache_dir / "imports"),
    ) if is_enabled(rules, "imports") else None
    struct_parser = StructParser(go_dir) if is_enabled(rules, "structures") else None
    
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
            # Merge proto structs (proto takes precedence)
            for struct_name, struct_def in proto_structs.items():
                struct_def['from_proto'] = True
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
        output_file=args.output
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


if __name__ == '__main__':
    main()
