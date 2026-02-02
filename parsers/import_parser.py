"""
Import Parser for Go code

Collects all imports used in the Go codebase and tries to extract:
- where each import is used (files)
- referenced selector symbols (pkg.Symbol)
- best-effort classification into "calls" vs "selectors"
- for local imports (within the same module), extracts type declarations (struct/interface/alias)
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from parsers.tree_sitter_helper import TreeSitterGoParser
from parsers.struct_parser import StructParser


def _is_stdlib_import(import_path: str) -> bool:
    # Heuristic: stdlib imports don't contain a dot in the first segment and usually don't contain a domain.
    # Examples:
    # - "fmt", "net/http", "encoding/json" => stdlib
    # - "github.com/x/y", "golang.org/x/..." => external
    # - "gitlab.company.local/group/proj/..." => external
    if not import_path:
        return True
    first = import_path.split("/")[0]
    return "." not in first


def _read_module_path(go_dir: Path) -> Optional[str]:
    go_mod = go_dir / "go.mod"
    if not go_mod.exists():
        return None
    try:
        content = go_mod.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.search(r"^module\s+(\S+)\s*$", content, re.MULTILINE)
    return m.group(1) if m else None


def _normalize_alias(alias: Optional[str], import_path: str) -> str:
    if alias and alias.strip():
        return alias.strip()
    # default alias is last segment
    return import_path.split("/")[-1]


def _extract_imports_from_content(content: str) -> List[Tuple[str, str]]:
    """
    Returns list of (alias, import_path)
    alias can be: "", "_", ".", "name"
    """
    results: List[Tuple[str, str]] = []

    # import "x/y"
    for m in re.finditer(r'^\s*import\s+"([^"]+)"\s*$', content, re.MULTILINE):
        results.append(("", m.group(1)))

    # import name "x/y"
    for m in re.finditer(r'^\s*import\s+([_.A-Za-z]\w*)\s+"([^"]+)"\s*$', content, re.MULTILINE):
        results.append((m.group(1), m.group(2)))

    # import ( ... ) blocks (can appear multiple times)
    for block in re.finditer(r'^\s*import\s*\((.*?)^\s*\)\s*$', content, re.MULTILINE | re.DOTALL):
        block_body = block.group(1)
        for line in block_body.splitlines():
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            # "x/y"
            m1 = re.match(r'^"([^"]+)"\s*(?://.*)?$', line)
            if m1:
                results.append(("", m1.group(1)))
                continue
            # name "x/y"  |  _ "x/y"  |  . "x/y"
            m2 = re.match(r'^([_.A-Za-z]\w*)\s+"([^"]+)"\s*(?://.*)?$', line)
            if m2:
                results.append((m2.group(1), m2.group(2)))
                continue

    # de-dup while preserving order
    seen = set()
    uniq: List[Tuple[str, str]] = []
    for a, p in results:
        key = (a, p)
        if key in seen:
            continue
        seen.add(key)
        uniq.append(key)
    return uniq


def _sanitize_path_component(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s)


def _guess_repo_root(import_path: str) -> Optional[str]:
    """
    Best-effort guess of repository root from Go import path.
    Supports common hosts:
    - github.com/<org>/<repo>/...
    - gitlab.com/<group>/<repo>/...
    - bitbucket.org/<org>/<repo>/...
    - generic: <host>/<a>/<b>/...
    """
    parts = import_path.split("/")
    if len(parts) < 3:
        return None
    host = parts[0]
    if "." not in host:
        return None
    # hosts that often require non-trivial VCS mapping
    if host in {"golang.org", "gopkg.in"}:
        return None
    return "/".join(parts[:3])


def _repo_root_to_clone_url(repo_root: str) -> str:
    return f"https://{repo_root}.git"


def _extract_selector_uses(content: str, alias: str) -> Tuple[Set[str], Set[str]]:
    """
    Extract best-effort symbol usage for `alias.Symbol`.
    Returns: (selectors, calls)
    """
    selectors: Set[str] = set()
    calls: Set[str] = set()

    # alias.Symbol
    sel_re = re.compile(rf"\b{re.escape(alias)}\.([A-Za-z_]\w*)")
    for m in sel_re.finditer(content):
        sym = m.group(1)
        selectors.add(sym)

    # alias.Symbol(
    call_re = re.compile(rf"\b{re.escape(alias)}\.([A-Za-z_]\w*)\s*\(")
    for m in call_re.finditer(content):
        calls.add(m.group(1))

    return selectors, calls


def _classify_type_candidates(content: str, alias: str, symbols: Set[str]) -> Set[str]:
    """
    Heuristic: consider symbol a "type candidate" if used as:
    - *alias.Type
    - alias.Type{
    - []alias.Type / map[...]alias.Type
    """
    type_syms: Set[str] = set()
    for sym in symbols:
        patterns = [
            rf"\*\s*{re.escape(alias)}\.{re.escape(sym)}\b",
            rf"\b{re.escape(alias)}\.{re.escape(sym)}\s*\{{",
            rf"\[\]\s*{re.escape(alias)}\.{re.escape(sym)}\b",
            rf"map\[[^\]]+\]\s*{re.escape(alias)}\.{re.escape(sym)}\b",
        ]
        for pat in patterns:
            if re.search(pat, content):
                type_syms.add(sym)
                break
    return type_syms


def _local_dir_for_import(go_dir: Path, module_path: Optional[str], import_path: str) -> Optional[Path]:
    if not module_path:
        return None
    if import_path == module_path:
        return go_dir
    if import_path.startswith(module_path + "/"):
        rel = import_path[len(module_path) + 1 :]
        return go_dir / rel
    return None


def _extract_local_types_from_dir(dir_path: Path) -> Dict[str, Dict]:
    """
    Returns dict: type_name -> {kind, file, ...}
    """
    if not dir_path.exists() or not dir_path.is_dir():
        return {}

    ts = TreeSitterGoParser()
    use_ts = ts.is_available()

    types: Dict[str, Dict] = {}
    go_files = [p for p in dir_path.glob("*.go") if not p.name.endswith("_test.go")]
    for f in go_files:
        try:
            content = f.read_text(encoding="utf-8")
            src = content.encode("utf-8")
        except Exception:
            continue

        if use_ts:
            tree = ts.parse_file(f)
            if not tree:
                continue
            type_decls = ts.find_nodes_by_type(tree, "type_declaration")
            for type_decl in type_decls:
                for child in type_decl.children:
                    if child.type != "type_spec":
                        continue
                    type_name = None
                    struct_node = None
                    iface_node = None
                    other_node = None
                    for gc in child.children:
                        if gc.type == "type_identifier":
                            type_name = ts.get_node_text(gc, src)
                        elif gc.type == "struct_type":
                            struct_node = gc
                        elif gc.type == "interface_type":
                            iface_node = gc
                        else:
                            # could be alias/defined type
                            if gc.type not in ("type_identifier",):
                                other_node = gc
                    if not type_name:
                        continue
                    if struct_node is not None:
                        fields = ts.extract_struct_fields(struct_node, src)
                        types[type_name] = {
                            "kind": "struct",
                            "fields": fields,
                            "file": str(f),
                            "line": struct_node.start_point[0] + 1,
                        }
                    elif iface_node is not None:
                        # Store raw interface text (best-effort)
                        types[type_name] = {
                            "kind": "interface",
                            "definition": ts.get_node_text(iface_node, src),
                            "file": str(f),
                            "line": iface_node.start_point[0] + 1,
                        }
                    elif other_node is not None:
                        types[type_name] = {
                            "kind": "type",
                            "definition": ts.get_node_text(other_node, src),
                            "file": str(f),
                            "line": other_node.start_point[0] + 1,
                        }
        else:
            # Regex fallback (struct only)
            for m in re.finditer(r"type\s+(\w+)\s+struct\s*\{([\s\S]*?)\n\}", content, re.MULTILINE):
                name = m.group(1)
                body = m.group(2)
                fields = []
                line = content[: m.start()].count("\n") + 1
                for line in body.splitlines():
                    line = line.strip()
                    if not line or line.startswith("//"):
                        continue
                    fm = re.match(r"(\w+)\s+([^\s`]+)(?:\s+`([^`]+)`)?", line)
                    if not fm:
                        continue
                    field_name = fm.group(1)
                    field_type = fm.group(2)
                    tags = fm.group(3) or ""
                    json_tag = None
                    if tags:
                        jm = re.search(r'json:"([^"]+)"', tags)
                        if jm:
                            json_tag = jm.group(1).split(",")[0]
                    if not json_tag:
                        json_tag = field_name
                    fields.append({"name": field_name, "type": field_type, "json_tag": json_tag})
                types[name] = {"kind": "struct", "fields": fields, "file": str(f), "line": line}

    return types


class ImportParser:
    def __init__(self, go_dir: Path, rules: Optional[Dict] = None, cache_dir: Optional[Path] = None):
        self.go_dir = go_dir
        self.rules = rules or {}
        self.cache_dir = cache_dir

    def parse(self) -> Dict:
        module_path = _read_module_path(self.go_dir)

        go_files = list(self.go_dir.rglob("*.go"))
        go_files = [
            f
            for f in go_files
            if not f.name.endswith("_test.go") and "vendor" not in str(f)
        ]

        imports: Dict[str, Dict] = {}
        local_types_cache: Dict[str, Dict[str, Dict]] = {}
        external_types_cache: Dict[str, Dict[str, Dict]] = {}

        import_clone_cfg = (self.rules.get("features") or {}).get("import_clone") or {}
        clone_enabled = bool(import_clone_cfg.get("enabled", False))
        max_repos = int(import_clone_cfg.get("max_repos", 8) or 8)
        host_allowlist = import_clone_cfg.get("hosts") or []
        overrides = import_clone_cfg.get("overrides") or {}

        if clone_enabled and self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        for go_file in go_files:
            try:
                content = go_file.read_text(encoding="utf-8")
            except Exception:
                continue

            file_imports = _extract_imports_from_content(content)
            if not file_imports:
                continue

            rel_file = str(go_file.relative_to(self.go_dir))

            for raw_alias, import_path in file_imports:
                alias = _normalize_alias(raw_alias, import_path)

                if import_path not in imports:
                    imports[import_path] = {
                        "path": import_path,
                        "is_stdlib": _is_stdlib_import(import_path),
                        "aliases": set(),
                        "files": {},
                        "used": {
                            "selectors": set(),
                            "calls": set(),
                            "type_candidates": set(),
                        },
                        "local": {
                            "is_local": False,
                            "dir": None,
                            "types": {},
                        },
                        "external": {
                            "repo_root": None,
                            "clone_url": None,
                            "cloned": False,
                            "error": None,
                            "types": {},
                        },
                    }

                imports[import_path]["aliases"].add(alias)

                file_entry = imports[import_path]["files"].setdefault(
                    rel_file,
                    {
                        "file": rel_file,
                        "aliases": set(),
                        "selectors": set(),
                        "calls": set(),
                        "type_candidates": set(),
                    },
                )
                file_entry["aliases"].add(alias)

                # dot/blank imports don't have selector usage
                if alias in {"_", "."}:
                    continue

                selectors, calls = _extract_selector_uses(content, alias)
                type_candidates = _classify_type_candidates(content, alias, selectors)

                file_entry["selectors"].update(selectors)
                file_entry["calls"].update(calls)
                file_entry["type_candidates"].update(type_candidates)

                imports[import_path]["used"]["selectors"].update(selectors)
                imports[import_path]["used"]["calls"].update(calls)
                imports[import_path]["used"]["type_candidates"].update(type_candidates)

                # Local types extraction (only once per import path)
                local_dir = _local_dir_for_import(self.go_dir, module_path, import_path)
                if local_dir is not None:
                    imports[import_path]["local"]["is_local"] = True
                    imports[import_path]["local"]["dir"] = str(local_dir.relative_to(self.go_dir))
                    if import_path not in local_types_cache:
                        local_types_cache[import_path] = _extract_local_types_from_dir(local_dir)
                    imports[import_path]["local"]["types"] = local_types_cache[import_path]

                # External repo enrichment (best effort)
                if (
                    clone_enabled
                    and self.cache_dir
                    and (not imports[import_path]["is_stdlib"])
                    and (local_dir is None)
                ):
                    repo_root = None
                    clone_url = None

                    # Overrides by prefix
                    for prefix, cfg in overrides.items():
                        if import_path.startswith(prefix):
                            repo_root = cfg.get("repo_root") or prefix
                            clone_url = cfg.get("clone_url")
                            break

                    if repo_root is None:
                        repo_root = _guess_repo_root(import_path)
                    if repo_root and clone_url is None:
                        clone_url = _repo_root_to_clone_url(repo_root)

                    if repo_root and clone_url:
                        if host_allowlist and repo_root.split("/")[0] not in host_allowlist:
                            pass
                        else:
                            imports[import_path]["external"]["repo_root"] = repo_root
                            imports[import_path]["external"]["clone_url"] = clone_url

                            if repo_root not in external_types_cache and len(external_types_cache) < max_repos:
                                repo_dir = self.cache_dir / _sanitize_path_component(repo_root)
                                try:
                                    if not repo_dir.exists():
                                        subprocess.run(
                                            ["git", "clone", "--depth", "1", "--quiet", clone_url, str(repo_dir)],
                                            check=True,
                                        )
                                    sp = StructParser(repo_dir)
                                    external_types_cache[repo_root] = sp.parse()
                                except Exception as e:
                                    external_types_cache[repo_root] = {}
                                    imports[import_path]["external"]["error"] = str(e)

                            if repo_root in external_types_cache:
                                imports[import_path]["external"]["cloned"] = True if external_types_cache[repo_root] else False
                                imports[import_path]["external"]["types"] = external_types_cache[repo_root]

        # Convert sets to lists for JSON-serializable dict
        for imp in imports.values():
            imp["aliases"] = sorted(imp["aliases"])
            imp["used"]["selectors"] = sorted(imp["used"]["selectors"])
            imp["used"]["calls"] = sorted(imp["used"]["calls"])
            imp["used"]["type_candidates"] = sorted(imp["used"]["type_candidates"])
            files = []
            for f in sorted(imp["files"].keys()):
                fe = imp["files"][f]
                fe["aliases"] = sorted(fe["aliases"])
                fe["selectors"] = sorted(fe["selectors"])
                fe["calls"] = sorted(fe["calls"])
                fe["type_candidates"] = sorted(fe["type_candidates"])
                files.append(fe)
            imp["files"] = files

        return {
            "module": module_path or "unknown",
            "imports": [imports[k] for k in sorted(imports.keys())],
        }

