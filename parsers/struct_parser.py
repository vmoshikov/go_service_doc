"""
Struct Parser for Go code

Extracts Go type declarations for:
- struct types (with fields + json tags)
- interface types (best effort)
- other named types (best effort)

Uses tree-sitter when available, falls back to regex for structs.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

from parsers.path_filter import is_path_excluded
from parsers.tree_sitter_helper import TreeSitterGoParser


class StructParser:
    def __init__(self, go_dir: Path, exclude_dirs: Optional[List[str]] = None):
        self.go_dir = go_dir
        self.exclude_dirs = exclude_dirs or []
        self.structs: Dict[str, Dict] = {}
        self.ts_parser = TreeSitterGoParser()
        self.use_tree_sitter = self.ts_parser.is_available()

    def parse(self) -> Dict[str, Dict]:
        go_files = list(self.go_dir.rglob("*.go"))
        go_files = [
            f for f in go_files
            if not f.name.endswith("_test.go")
            and not is_path_excluded(str(f.relative_to(self.go_dir)), self.exclude_dirs)
        ]
        for go_file in go_files:
            if self.use_tree_sitter:
                self._parse_file_tree_sitter(go_file)
            else:
                self._parse_file_regex(go_file)
        return self.structs

    def _parse_file_tree_sitter(self, go_file: Path):
        try:
            content = go_file.read_text(encoding="utf-8")
            source_bytes = content.encode("utf-8")
        except Exception:
            return

        tree = self.ts_parser.parse_file(go_file)
        if not tree:
            self._parse_file_regex(go_file)
            return

        type_decls = self.ts_parser.find_nodes_by_type(tree, "type_declaration")
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
                        type_name = self.ts_parser.get_node_text(gc, source_bytes)
                    elif gc.type == "struct_type":
                        struct_node = gc
                    elif gc.type == "interface_type":
                        iface_node = gc
                    else:
                        if gc.type not in ("type_identifier",):
                            other_node = gc
                if not type_name:
                    continue

                rel = str(go_file.relative_to(self.go_dir))
                # Best-effort line number for the type definition
                line = None
                try:
                    # Prefer the concrete node; fallback to type_spec
                    node_for_line = struct_node or iface_node or other_node or child
                    line = node_for_line.start_point[0] + 1  # 1-based
                except Exception:
                    line = None

                if struct_node is not None:
                    fields = self.ts_parser.extract_struct_fields(struct_node, source_bytes)
                    self.structs[type_name] = {"kind": "struct", "fields": fields, "file": rel, "line": line}
                elif iface_node is not None:
                    self.structs[type_name] = {
                        "kind": "interface",
                        "definition": self.ts_parser.get_node_text(iface_node, source_bytes),
                        "file": rel,
                        "line": line,
                    }
                elif other_node is not None:
                    self.structs[type_name] = {
                        "kind": "type",
                        "definition": self.ts_parser.get_node_text(other_node, source_bytes),
                        "file": rel,
                        "line": line,
                    }

    def _parse_file_regex(self, go_file: Path):
        try:
            content = go_file.read_text(encoding="utf-8")
        except Exception:
            return

        # struct only fallback
        for m in re.finditer(r"type\s+(\w+)\s+struct\s*\{([\s\S]*?)\n\}", content, re.MULTILINE):
            name = m.group(1)
            body = m.group(2)
            fields: List[Dict] = []
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

            self.structs[name] = {
                "kind": "struct",
                "fields": fields,
                "file": str(go_file.relative_to(self.go_dir)),
                "line": line,
            }

