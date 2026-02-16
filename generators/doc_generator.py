"""
Documentation Generator

Combines user-provided documentation sections with auto-generated content
to create a comprehensive README.md file.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional

from generators.ai_description import generate_function_description, generate_endpoint_description
from generators.plantuml_generator import PlantUMLGenerator
from parsers.component_analyzer import ComponentAnalyzer
from rules import is_enabled


class DocumentationGenerator:
    def __init__(
        self,
        go_dir: Path,
        docs_dir: Path,
        user_docs_dir: Optional[Path] = None,
        repo_name: Optional[str] = None,
        repo_ref: Optional[str] = None,
        repo_web_url: Optional[str] = None,
        rules: Optional[Dict] = None,
    ):
        self.go_dir = go_dir
        self.docs_dir = docs_dir
        self.sections_dir = self.docs_dir / "sections"
        self.diagrams_dir = self.docs_dir / "diagrams"
        self.sections_dir.mkdir(parents=True, exist_ok=True)
        self.diagrams_dir.mkdir(parents=True, exist_ok=True)
        # Optional user-provided docs directory; if not set, defaults to docs_dir
        self.user_docs_dir = user_docs_dir
        self.structs = {}  # Will be set from API spec
        self.plantuml_generator = PlantUMLGenerator()
        self.repo_name = repo_name
        self.repo_ref = repo_ref
        self.repo_web_url = repo_web_url
        self.rules = rules or {}
    
    def set_structs(self, structs: Dict):
        """Set struct definitions for JSON generation."""
        self.structs = structs
    
    def _create_file_link(self, file_path: str, line: Optional[int] = None) -> str:
        """Create a clickable link to a file with optional line number."""
        label = f"{file_path}:{line}" if line else file_path

        # If we have a web URL, try to create a web link to source.
        if self.repo_web_url and self.repo_ref:
            base = self.repo_web_url.rstrip("/")
            # GitLab commonly uses /-/blob/<ref>/<path>
            if "gitlab" in base or "/-/" in base:
                url = f"{base}/-/blob/{self.repo_ref}/{file_path}"
            else:
                # GitHub-style /blob/<ref>/<path>
                url = f"{base}/blob/{self.repo_ref}/{file_path}"
            if line:
                url += f"#L{line}"
            return f"[`{label}`]({url})"

        # Default: do not create broken relative links in docs repo
        return f"`{label}`"
    
    def _create_anchor_link(self, text: str) -> str:
        """Create an anchor link from text (for navigation).
        Uses GitHub's anchor generation algorithm."""
        import re
        import unicodedata
        
        # Remove markdown formatting (links, code, bold, italic)
        # Extract text from markdown links: [text](url) -> text
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        # Remove code formatting: `code` -> code
        text = re.sub(r'`([^`]+)`', r'\1', text)
        # Remove bold/italic: **text** -> text, *text* -> text
        text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
        text = re.sub(r'\*([^\*]+)\*', r'\1', text)
        
        # Convert to lowercase
        anchor = text.lower()
        
        # Replace spaces with hyphens
        anchor = anchor.replace(' ', '-')
        
        # Remove special characters (keep only alphanumeric, hyphens, underscores)
        anchor = re.sub(r'[^\w\-]', '', anchor)
        
        # Remove consecutive hyphens
        anchor = re.sub(r'-+', '-', anchor)
        
        # Remove leading/trailing hyphens
        anchor = anchor.strip('-')
        
        return anchor
    
    def generate(
        self,
        functions: List[Dict],
        api_spec: Dict,
        tests: Dict,
        libraries: Dict,
        imports: Optional[Dict] = None,
        output_file: str = 'README.md'
    ):
        """Generate complete documentation."""
        
        # Set structs for JSON generation
        self.structs = api_spec.get('structs', {})

        component_info = None
        if is_enabled(self.rules, "diagrams"):
            print("Analyzing components and dependencies...")
            component_analyzer = ComponentAnalyzer(self.go_dir)
            component_info = component_analyzer.analyze()
            self._generate_diagrams(component_info, api_spec)

        # Generate individual sections (only enabled)
        if is_enabled(self.rules, "functions"):
            self._generate_functions(functions, api_spec)
        if is_enabled(self.rules, "structures"):
            self._generate_structures(api_spec.get("structs", {}) or {})
        if is_enabled(self.rules, "api"):
            self._generate_api_spec(api_spec)
        if is_enabled(self.rules, "tests"):
            self._generate_tests(tests)
        if is_enabled(self.rules, "libraries"):
            self._generate_libraries(libraries)
        if is_enabled(self.rules, "imports"):
            self._generate_imports(imports or {})

        # Ensure standard top-level files exist
        self._ensure_top_level_files()

        # Combine README (always, but content depends on rules)
        self._combine_sections(output_file, component_info)

    def _ensure_top_level_files(self):
        """Ensure docs/<repo_name>/ has standard files."""
        # RULES.md snapshot (do not override user edits)
        rules_path = self.docs_dir / "RULES.md"
        if not rules_path.exists():
            snapshot = dict(self.rules or {})
            repo_info = dict(snapshot.get("repo", {}) or {})
            if self.repo_name:
                repo_info.setdefault("name", self.repo_name)
            if self.repo_ref:
                repo_info.setdefault("ref", self.repo_ref)
            if self.repo_web_url:
                repo_info.setdefault("web_url", self.repo_web_url)
            if repo_info:
                snapshot["repo"] = repo_info

            content = ["# RULES\n\n"]
            content.append("Этот файл сгенерирован автоматически и отражает применённые правила генерации.\n\n")
            content.append("```json\n")
            content.append(json.dumps(snapshot, indent=2, ensure_ascii=False))
            content.append("\n```\n")
            rules_path.write_text("".join(content), encoding="utf-8")

        # CHANGELOG.md placeholder (if changelog generator is not used)
        changelog_path = self.docs_dir / "CHANGELOG.md"
        if not changelog_path.exists():
            changelog_path.write_text(
                "# CHANGELOG\n\n"
                "Этот файл зарезервирован под changelog. Если он не генерируется автоматически, заполните вручную.\n",
                encoding="utf-8",
            )

    def _sections_nav(self, current_depth: int = 1) -> List[str]:
        """
        Navigation block for section files.
        current_depth:
          - 1 for docs/<repo>/sections/*.md (../README.md)
          - 2 for docs/<repo>/sections/functions/*.md (../../README.md)
        """
        prefix = "../" * current_depth
        lines: List[str] = []
        lines.append("## Навигация\n\n")
        lines.append(f"- [К оглавлению документации]({prefix}README.md)\n")
        lines.append(f"- [Диаграммы]({prefix}diagrams/)\n")
        lines.append("- [Импорты](imports.md)\n")
        lines.append("- [Структуры и типы](structures.md)\n")
        lines.append("- [Функции](functions.md)\n")
        lines.append("- [Спецификация API](api.md)\n")
        lines.append("- [Тестирование](tests.md)\n")
        lines.append("- [Используемые библиотеки](libraries.md)\n")
        lines.append("\n---\n\n")
        return lines

    def _generate_imports(self, imports: Dict):
        """Generate imports.md (imports overview)."""
        content = ["# Импорты\n\n"]
        content.extend(self._sections_nav(current_depth=1))

        module = imports.get("module") if isinstance(imports, dict) else None
        if module:
            content.append(f"**Модуль:** `{module}`\n\n")

        import_list = imports.get("imports", []) if isinstance(imports, dict) else []
        if not import_list:
            content.append("Импорты не найдены.\n")
            (self.sections_dir / "imports.md").write_text("\n".join(content), encoding="utf-8")
            return

        content.append("Файл сгенерирован из Go‑исходников и показывает использование импортов.\n\n")

        # Group imports for better menu (H2 sections in README)
        stdlib = [i for i in import_list if i.get("is_stdlib")]
        non_stdlib = [i for i in import_list if not i.get("is_stdlib")]
        local = [i for i in non_stdlib if (i.get("local") or {}).get("is_local")]
        external = [i for i in non_stdlib if i not in local]

        groups = [
            ("Стандартная библиотека", stdlib),
            ("Внешние зависимости", external),
            ("Локальные пакеты", local),
        ]

        for group_title, group_items in groups:
            if not group_items:
                continue
            content.append(f"## {group_title}\n\n")

            for imp in group_items:
                path = imp.get("path", "")
                is_stdlib = imp.get("is_stdlib", False)
                aliases = imp.get("aliases", [])
                used = imp.get("used", {}) or {}
                files = imp.get("files", []) or []
                local = imp.get("local", {}) or {}
                external = imp.get("external", {}) or {}

                content.append(f"### {path}\n\n")
                content.append(
                    f"- **Тип:** {'stdlib' if is_stdlib else ('local' if local.get('is_local') else 'external')}\n"
                )
                if aliases:
                    content.append(f"- **Алиасы:** {', '.join(f'`{a}`' for a in aliases)}\n")
                if local.get("is_local"):
                    content.append(f"- **Локальная директория пакета:** `{local.get('dir')}`\n")
                if external.get("repo_root"):
                    content.append(f"- **📥 Repo:** `{external.get('repo_root')}`\n")
                    if external.get("clone_url"):
                        content.append(f"- **🔗 Clone URL:** `{external.get('clone_url')}`\n")
                    if external.get("error"):
                        content.append(f"- **⚠️ Ошибка клонирования/парсинга:** `{external.get('error')}`\n")
                content.append("\n")

                selectors = used.get("selectors", []) or []
                calls = used.get("calls", []) or []
                type_candidates = used.get("type_candidates", []) or []

                if calls:
                    content.append("### Вызовы\n\n")
                    content.append(", ".join(f"`{s}`" for s in sorted(set(calls))) + "\n\n")

                if type_candidates:
                    content.append("### Кандидаты на типы\n\n")
                    content.append(", ".join(f"`{s}`" for s in sorted(set(type_candidates))) + "\n\n")

                if selectors:
                    content.append("### Селекторы (любое использование `pkg.X`)\n\n")
                    content.append(", ".join(f"`{s}`" for s in sorted(set(selectors))) + "\n\n")

                if files:
                    content.append("### Используется в файлах\n\n")
                    for fe in files:
                        file_path = fe.get("file")
                        content.append(f"- 📄 {self._create_file_link(file_path)}\n")
                    content.append("\n")

                # If this is a local import, try to print definitions of referenced types.
                local_types = (local.get("types") or {}) if isinstance(local, dict) else {}
                if local.get("is_local") and local_types and type_candidates:
                    content.append("### Определения локальных типов (best effort)\n\n")
                    for t in sorted(set(type_candidates)):
                        info = local_types.get(t)
                        if not info:
                            continue
                        kind = info.get("kind", "type")
                        src_file = info.get("file")
                        src_line = info.get("line")
                        content.append(f"#### {t} ({kind})\n\n")
                        if src_file:
                            try:
                                rel = str(Path(src_file).relative_to(self.go_dir))
                            except Exception:
                                rel = str(src_file)
                            content.append(f"*Определено в: {self._create_file_link(rel, src_line)}*\n\n")
                        if kind == "struct":
                            fields = info.get("fields", []) or []
                            if fields:
                                content.append("| Поле | Тип | JSON |\n")
                                content.append("|------|-----|------|\n")
                                for f in fields:
                                    content.append(
                                        f"| `{f.get('name','')}` | `{f.get('type','')}` | `{f.get('json_tag','')}` |\n"
                                    )
                                content.append("\n")
                        else:
                            definition = info.get("definition")
                            if definition:
                                content.append("```go\n")
                                content.append(definition)
                                content.append("\n```\n\n")

                # External repo types (if cloned)
                ext_types = (external.get("types") or {}) if isinstance(external, dict) else {}
                if (not local.get("is_local")) and ext_types and type_candidates:
                    content.append("### Определения типов из внешнего репозитория (best effort)\n\n")
                    for t in sorted(set(type_candidates)):
                        info = ext_types.get(t)
                        if not info:
                            continue
                        kind = info.get("kind", "type")
                        src_file = info.get("file")
                        src_line = info.get("line")
                        content.append(f"#### {t} ({kind})\n\n")
                        if src_file:
                            label = f"{src_file}:{src_line}" if src_line else src_file
                            content.append(f"*Определено в:* `{label}`\n\n")
                        if kind == "struct":
                            fields = info.get("fields", []) or []
                            if fields:
                                content.append("| Поле | Тип | JSON |\n")
                                content.append("|------|-----|------|\n")
                                for f in fields:
                                    content.append(
                                        f"| `{f.get('name','')}` | `{f.get('type','')}` | `{f.get('json_tag','')}` |\n"
                                    )
                                content.append("\n")
                        else:
                            definition = info.get("definition")
                            if definition:
                                content.append("```go\n")
                                content.append(definition)
                                content.append("\n```\n\n")

        content.append("\n---\n\n")
        content.extend(self._sections_nav(current_depth=1))
        (self.sections_dir / "imports.md").write_text("\n".join(content), encoding="utf-8")

    def _generate_structures(self, structs: Dict):
        """Generate structures.md (all types/structs)."""
        content = ["# Структуры и типы\n\n"]
        content.extend(self._sections_nav(current_depth=1))

        if not structs:
            content.append("Структуры/типы не найдены.\n")
            (self.sections_dir / "structures.md").write_text("\n".join(content), encoding="utf-8")
            return

        # Group by first-level directory of definition file
        grouped: Dict[str, List[tuple]] = {}
        for name, info in structs.items():
            file_path = info.get("file", "")
            top = file_path.split("/", 1)[0] if "/" in file_path else "."
            grouped.setdefault(top, []).append((name, info))

        content.append("## Меню\n\n")
        for top in sorted(grouped.keys()):
            title = "root" if top == "." else top
            content.append(f"- 📁 [{title}](#{self._create_anchor_link(title)})\n")
        content.append("\n---\n\n")

        for top in sorted(grouped.keys()):
            title = "root" if top == "." else top
            content.append(f"## {title}\n\n")
            for name, info in sorted(grouped[top], key=lambda x: x[0]):
                kind = info.get("kind", "type")
                file_path = info.get("file")
                line = info.get("line")
                content.append(f"### {name} ({kind})\n\n")
                if file_path:
                    content.append(f"- 📍 *Определено в:* {self._create_file_link(file_path, line)}\n")
                if kind == "struct":
                    fields = info.get("fields", []) or []
                    if fields:
                        content.append("\n| Поле | Тип | JSON |\n")
                        content.append("|------|-----|------|\n")
                        for f in fields:
                            content.append(
                                f"| `{f.get('name','')}` | `{f.get('type','')}` | `{f.get('json_tag','')}` |\n"
                            )
                        content.append("\n")
                    # Add JSON example
                    struct_json = self._struct_to_json(info)
                    if struct_json:
                        content.append("**Пример (JSON):**\n\n")
                        content.append("```json")
                        content.append(json.dumps(struct_json, indent=2, ensure_ascii=False))
                        content.append("```\n\n")
                else:
                    definition = info.get("definition")
                    if definition:
                        content.append("\n```go\n")
                        content.append(definition)
                        content.append("\n```\n\n")

            content.append("\n")

        content.append("\n---\n\n")
        content.extend(self._sections_nav(current_depth=1))
        (self.sections_dir / "structures.md").write_text("\n".join(content), encoding="utf-8")
    
    def _get_struct_json_for_type(self, type_name: str) -> Optional[Dict]:
        """Get JSON representation of a struct type."""
        # Try exact match
        if type_name in self.structs:
            return self._struct_to_json(self.structs[type_name])
        
        # Try without package prefix
        clean_name = type_name.split('.')[-1]
        if clean_name in self.structs:
            return self._struct_to_json(self.structs[clean_name])
        
        # Try searching by partial name
        for key in self.structs.keys():
            if key.endswith(clean_name) or clean_name in key:
                return self._struct_to_json(self.structs[key])
        
        return None
    
    def _struct_to_json(self, struct_info: Dict) -> Dict:
        """Convert struct info to JSON representation."""
        json_obj = {}
        
        for field in struct_info.get('fields', []):
            json_key = field.get('json_tag')
            if not json_key or json_key == '-' or json_key.startswith('XXX_'):
                continue
            
            json_type = self._go_type_to_json_type(field.get('type', ''))
            json_obj[json_key] = json_type
        
        return json_obj
    
    def _go_type_to_json_type(self, go_type: str):
        """Convert Go type to JSON representation."""
        import re
        go_type = go_type.strip()
        
        type_mapping = {
            'string': 'string',
            'int': 0, 'int8': 0, 'int16': 0, 'int32': 0, 'int64': 0,
            'uint': 0, 'uint8': 0, 'uint16': 0, 'uint32': 0, 'uint64': 0,
            'float32': 0.0, 'float64': 0.0,
            'bool': False,
            'time.Time': '2023-01-01T00:00:00Z',
            'time.Duration': '1s',
        }
        
        if go_type in type_mapping:
            return type_mapping[go_type]
        
        if go_type.startswith('*'):
            inner_type = go_type[1:].strip()
            if inner_type in type_mapping:
                return type_mapping[inner_type]
            return None
        
        if go_type.startswith('[]'):
            return []
        
        if go_type.startswith('map['):
            return {}
        
        if 'Duration' in go_type:
            return '1s'
        
        return {}
    
    def _generate_functions(self, functions: List[Dict], api_spec: Dict):
        """Generate functions index + per-top-level-directory files."""
        if not functions:
            content = ["# Функции\n\nФункции не найдены.\n"]
            (self.sections_dir / "functions.md").write_text("\n".join(content), encoding="utf-8")
            return

        # Group by first-level directory (top-level)
        grouped: Dict[str, List[Dict]] = {}
        for func in functions:
            fp = func.get("file", "")
            top = fp.split("/", 1)[0] if "/" in fp else "."
            grouped.setdefault(top, []).append(func)

        functions_dir = self.sections_dir / "functions"
        functions_dir.mkdir(parents=True, exist_ok=True)

        def safe_name(s: str) -> str:
            import re
            s = s.strip().replace("/", "_").replace("\\", "_")
            s = re.sub(r"[^A-Za-z0-9_.-]+", "_", s)
            return s or "root"

        def func_heading(file_path: str, line: Optional[int], name: str) -> str:
            # Unique heading text to make anchors stable (no raw HTML anchors)
            ln = line or 0
            return f"{name} ({file_path}:{ln})"

        # Prepare per-top-level directory pages
        dir_items: List[Dict[str, object]] = []
        for top in sorted(grouped.keys()):
            title = "root" if top == "." else top
            file_name = f"{safe_name(title)}.md"
            rel_path = f"sections/functions/{file_name}"
            dir_items.append(
                {
                    "key": top,
                    "dir": title,
                    "file_name": file_name,
                    "rel_path": rel_path,
                    "functions": grouped[top],
                }
            )

        def nav_block(prev_rel: Optional[str], next_rel: Optional[str]) -> List[str]:
            lines: List[str] = []
            lines.append("## Навигация\n\n")
            lines.append("- [К оглавлению документации](../../README.md)\n")
            lines.append("- [К индексу функций](../functions.md)\n")
            lines.append("- [К разделам](../)\n")
            if prev_rel:
                lines.append(f"- [Предыдущая директория]({prev_rel})\n")
            if next_rel:
                lines.append(f"- [Следующая директория]({next_rel})\n")
            lines.append("\n---\n\n")
            return lines

        # 1) Write per-top-level directory files with cross-links
        for i, item in enumerate(dir_items):
            title = item["dir"]  # type: ignore[assignment]
            file_name = item["file_name"]  # type: ignore[assignment]
            out_path = functions_dir / str(file_name)

            prev_rel = dir_items[i - 1]["file_name"] if i > 0 else None
            next_rel = dir_items[i + 1]["file_name"] if i + 1 < len(dir_items) else None

            page: List[str] = [f"# Функции: {title}\n\n"]
            page.extend(nav_block(str(prev_rel) if prev_rel else None, str(next_rel) if next_rel else None))
            
            # Group by file within this top-level directory
            by_file: Dict[str, List[Dict]] = {}
            for f in item["functions"]:  # type: ignore[index]
                by_file.setdefault(f["file"], []).append(f)

            # Menu: files in header
            page.append("## Меню по файлам\n\n")
            for file_path in sorted(by_file.keys()):
                anchor = self._create_anchor_link(file_path)
                page.append(f"- 📄 [{file_path}](#{anchor})\n")
            page.append("\n---\n\n")

            # Content: files with expandable function lists
            for file_path in sorted(by_file.keys()):
                anchor = self._create_anchor_link(file_path)
                page.append(f"## {file_path}\n\n")
                page.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of functions
                page.append(f"<details open>\n<summary><b>Функции в этом файле ({len(by_file[file_path])})</b></summary>\n\n")
                for func in sorted(by_file[file_path], key=lambda x: (x.get("name", ""), x.get("line", 0))):
                    heading = func_heading(file_path, func.get("line"), func.get("name", ""))
                    heading_anchor = self._create_anchor_link(heading)
                    func_name = func.get('name', '')
                    line = func.get('line')
                    if line:
                        page.append(f"- 🔗 [{func_name}](#{heading_anchor}) `:{line}`\n")
                    else:
                        page.append(f"- 🔗 [{func_name}](#{heading_anchor})\n")
                page.append("\n</details>\n\n")

                # Function details
                for func in sorted(by_file[file_path], key=lambda x: (x.get("name", ""), x.get("line", 0))):
                    heading = func_heading(file_path, func.get("line"), func.get("name", ""))
                    page.append(f"### {heading}\n\n")

                    description = func.get("comment", "").strip()
                    if not description:
                        description = generate_function_description(
                            func_name=func["name"],
                            params=func.get("params", ""),
                            returns=func.get("returns", ""),
                            receiver=func.get("receiver"),
                            file_path=func.get("file"),
                        )
                    if description:
                        page.append(f"{description}\n\n")

                    sig_parts = []
                    if func.get("receiver"):
                        sig_parts.append(f"func {func['receiver']}")
                    else:
                        sig_parts.append("func")
                    sig_parts.append(f"{func['name']}({func.get('params','')})")
                    if func.get("returns"):
                        sig_parts.append(func["returns"])

                    page.append(f"```go\n{' '.join(sig_parts)}\n```\n\n")

                    struct_types = func.get("struct_types", {}) or {}
                    if struct_types.get("request") or struct_types.get("response"):
                        for struct_type in struct_types.get("request", []):
                            struct_json = self._get_struct_json_for_type(struct_type)
                            if struct_json:
                                page.append(f"**Тип запроса:** {struct_type}\n\n")
                                page.append("```json")
                                page.append(json.dumps(struct_json, indent=2, ensure_ascii=False))
                                page.append("```\n\n")
                        for struct_type in struct_types.get("response", []):
                            struct_json = self._get_struct_json_for_type(struct_type)
                            if struct_json:
                                page.append(f"**Тип ответа:** {struct_type}\n\n")
                                page.append("```json")
                                page.append(json.dumps(struct_json, indent=2, ensure_ascii=False))
                                page.append("```\n\n")

                    page.append(f"📍 *Расположение:* {self._create_file_link(file_path, func.get('line'))}\n\n")

                page.append("\n")

            # Footer navigation
            page.append("\n---\n\n")
            page.extend(nav_block(str(prev_rel) if prev_rel else None, str(next_rel) if next_rel else None))
            out_path.write_text("\n".join(page), encoding="utf-8")

        # 2) Write index file (sections/functions.md)
        index: List[str] = ["# Функции\n\n"]
        index.extend(self._sections_nav(current_depth=1))
        index.append("## Директории верхнего уровня\n\n")
        index.append("- [К оглавлению документации](../README.md)\n\n")
        for item in dir_items:
            index.append(f"- 📁 [{item['dir']}]({item['rel_path']})\n")
        index.append("\n---\n\n")
        # Add H2 entries so main README can build a menu from this file if needed
        for item in dir_items:
            index.append(f"## {item['dir']}\n\n")
            index.append(f"- 📄 Подробнее: [{item['rel_path']}]({item['rel_path']})\n\n")
        index.append("\n---\n\n")
        index.extend(self._sections_nav(current_depth=1))

        (self.sections_dir / "functions.md").write_text("\n".join(index), encoding="utf-8")
    
    def _generate_directory_readme(self, dir_key: str, functions: List[Dict]) -> Dict:
        """Generate README.md for a specific directory."""
        content = []
        
        # Title based on directory
        if dir_key == '.':
            title = "# Функции корня проекта\n"
            dir_display = "root"
        else:
            title = f"# Функции в `{dir_key}`\n"
            dir_display = dir_key
        
        content.append(title)
        content.append(f"В этой директории найдено функций: {len(functions)}.\n\n")
        content.append("---\n\n")
        
        # Group by file within directory
        functions_by_file = {}
        for func in functions:
            file_path = Path(func['file'])
            file_name = file_path.name
            if file_name not in functions_by_file:
                functions_by_file[file_name] = []
            functions_by_file[file_name].append(func)
        
        for file_name, file_funcs in sorted(functions_by_file.items()):
            # Get full file path for link
            if dir_key == '.':
                full_file_path = file_name
            else:
                full_file_path = f"{dir_key}/{file_name}"
            
            file_link = self._create_file_link(full_file_path)
            content.append(f"## {file_link}\n\n")
            
            for func in file_funcs:
                content.append(f"### {func['name']}\n")
                
                # Use existing comment or generate description
                description = func.get('comment', '').strip()
                if not description:
                    description = generate_function_description(
                        func_name=func['name'],
                        params=func.get('params', ''),
                        returns=func.get('returns', ''),
                        receiver=func.get('receiver'),
                        file_path=func.get('file')
                    )
                
                if description:
                    content.append(f"{description}\n\n")
                
                # Function signature
                sig_parts = []
                if func['receiver']:
                    sig_parts.append(f"func {func['receiver']}")
                else:
                    sig_parts.append("func")
                
                sig_parts.append(f"{func['name']}({func['params']})")
                
                if func['returns']:
                    sig_parts.append(func['returns'])
                
                content.append(f"```go\n{' '.join(sig_parts)}\n```\n\n")
                
                # Show struct types if present
                struct_types = func.get('struct_types', {})
                if struct_types.get('request') or struct_types.get('response'):
                    # Request structs
                    for struct_type in struct_types.get('request', []):
                        struct_json = self._get_struct_json_for_type(struct_type)
                        if struct_json:
                            content.append(f"**Тип запроса: `{struct_type}`**\n\n")
                            content.append("```json")
                            content.append(json.dumps(struct_json, indent=2))
                            content.append("```\n\n")
                    
                    # Response structs
                    for struct_type in struct_types.get('response', []):
                        struct_json = self._get_struct_json_for_type(struct_type)
                        if struct_json:
                            content.append(f"**Тип ответа: `{struct_type}`**\n\n")
                            content.append("```json")
                            content.append(json.dumps(struct_json, indent=2))
                            content.append("```\n\n")
                
                # Location link
                if dir_key == '.':
                    full_file_path = file_name
                else:
                    full_file_path = f"{dir_key}/{file_name}"
                file_link = self._create_file_link(full_file_path, func.get('line'))
                content.append(f"*Расположение: {file_link}*\n\n")
        
        # Write directory docs only under docs_dir (do not modify analyzed repo)
        functions_root = self.docs_dir / "functions"
        if dir_key == '.':
            readme_path = functions_root / "root.md"
        else:
            readme_path = functions_root / dir_key / "README.md"
        readme_path.parent.mkdir(parents=True, exist_ok=True)
        
        readme_path.write_text('\n'.join(content), encoding='utf-8')
        
        # Return relative path from docs_dir for linking
        rel_path = str(readme_path.relative_to(self.docs_dir))
        
        return {
            'path': rel_path,
            'dir': dir_display,
            'function_count': len(functions)
        }
    
    def _generate_parent_functions_md(self, functions_by_dir: Dict, directory_readmes: Dict):
        """Generate parent functions.md with links to directory READMEs."""
        content = ["# Функции\n"]
        content.append("Функции сгруппированы по директориям. Откройте директорию, чтобы увидеть подробную документацию.\n\n")
        content.append("## Индекс директорий\n\n")
        
        for dir_key in sorted(functions_by_dir.keys()):
            dir_funcs = functions_by_dir[dir_key]
            dir_readme = directory_readmes.get(dir_key, {})
            
            if dir_key == '.':
                dir_display = "Root"
                readme_path = dir_readme.get('path', 'functions/root.md')
            else:
                dir_display = dir_key
                readme_path = dir_readme.get('path', f"functions/{dir_key}/README.md")
            
            func_count = len(dir_funcs)
            content.append(f"### {dir_display}\n")
            content.append(f"- **Функций:** {func_count}\n")
            content.append(f"- **Документация:** [{readme_path}]({readme_path})\n\n")
            
            # List functions in this directory (group by name to avoid duplicates)
            content.append("**Функции:**\n")
            
            # Group functions by name
            functions_by_name = {}
            for func in dir_funcs:
                func_name = func['name']
                if func_name not in functions_by_name:
                    functions_by_name[func_name] = []
                functions_by_name[func_name].append(func)
            
            # Display each function once with all locations and descriptions
            for func_name in sorted(functions_by_name.keys()):
                func_instances = functions_by_name[func_name]
                
                # Use first instance for description and link
                first_func = func_instances[0]
                
                # Generate description if missing
                description = first_func.get('comment', '').strip()
                if not description:
                    description = generate_function_description(
                        func_name=func_name,
                        params=first_func.get('params', ''),
                        returns=first_func.get('returns', ''),
                        receiver=first_func.get('receiver'),
                        file_path=first_func.get('file')
                    )
                
                # Create link to function in directory README
                func_link = f"{readme_path}#{self._create_anchor_link(func_name)}"
                
                if len(func_instances) == 1:
                    # Single instance - simple format with description
                    func = func_instances[0]
                    file_path = func['file']
                    line = func.get('line')
                    content.append(f"- [{func_name}]({func_link}) - {file_path}")
                    if line:
                        content[-1] += f":{line}"
                    content[-1] += f" - *{description}*\n"
                else:
                    # Multiple instances - show function name with description and all locations
                    content.append(f"- [{func_name}]({func_link}) - *{description}*\n")
                    for func in sorted(func_instances, key=lambda x: (x['file'], x.get('line', 0))):
                        file_path = func['file']
                        line = func.get('line')
                        content.append(f"  - {file_path}")
                        if line:
                            content[-1] += f":{line}"
                        content[-1] += "\n"
            
            content.append("\n")
        
        output_path = self.sections_dir / 'functions.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_api_spec(self, api_spec: Dict):
        """Generate api.md"""
        content = ["# Спецификация API\n\n"]
        content.extend(self._sections_nav(current_depth=1))
        
        # Collect all files with endpoints
        files_grpc: Dict[str, List[Dict]] = {}
        files_rest: Dict[str, List[Dict]] = {}
        
        if api_spec.get('grpc'):
            for endpoint in api_spec['grpc']:
                file_path = endpoint.get('file', '')
                files_grpc.setdefault(file_path, []).append(endpoint)
        
        if api_spec.get('rest'):
            for endpoint in api_spec['rest']:
                file_path = endpoint.get('file', '')
                files_rest.setdefault(file_path, []).append(endpoint)
        
        all_files = sorted(set(list(files_grpc.keys()) + list(files_rest.keys())))
        
        # Menu by files
        if all_files:
            content.append("## Меню по файлам\n\n")
            for file_path in all_files:
                anchor = self._create_anchor_link(file_path)
                content.append(f"- 📄 [{file_path}](#{anchor})\n")
            content.append("\n---\n\n")
        
        # gRPC endpoints grouped by file
        if api_spec.get('grpc'):
            content.append("## gRPC методы\n\n")
            
            for file_path in sorted(files_grpc.keys()):
                anchor = self._create_anchor_link(file_path)
                content.append(f"### {file_path}\n\n")
                content.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of endpoints
                endpoints_list = files_grpc[file_path]
                content.append(f"<details open>\n<summary><b>Методы в этом файле ({len(endpoints_list)})</b></summary>\n\n")
                for endpoint in sorted(endpoints_list, key=lambda x: x.get('method', '')):
                    method = endpoint['method']
                    method_anchor = self._create_anchor_link(method)
                    content.append(f"- 🔗 [{method}](#{method_anchor})\n")
                content.append("\n</details>\n\n")
                
                # Endpoint details
                for endpoint in sorted(endpoints_list, key=lambda x: x.get('method', '')):
                    content.append(f"#### {endpoint['method']}\n\n")
                    
                    # Use existing comment or generate description
                    description = endpoint.get('comment', '').strip()
                    if not description:
                        description = generate_endpoint_description(
                            method=endpoint['method'],
                            request_type=endpoint.get('request_type'),
                            response_type=endpoint.get('response_type')
                        )
                    
                    if description:
                        content.append(f"{description}\n\n")
                    
                    # Request type with external link if available
                    request_type = endpoint.get('request_type', '')
                    request_display = f"**Тип запроса:** `{request_type}`"
                    if endpoint.get('proto_link'):
                        proto_link = endpoint['proto_link']
                        request_display += f" - [Открыть proto]({proto_link})"
                    content.append(f"{request_display}\n")
                    
                    # Response type with external link if available
                    response_type = endpoint.get('response_type', '')
                    response_display = f"**Тип ответа:** `{response_type}`"
                    if endpoint.get('proto_link'):
                        response_display += f" - [Открыть proto]({endpoint['proto_link']})"
                    content.append(f"{response_display}\n\n")
                    
                    # Add proto repository info if available
                    if endpoint.get('proto_repo'):
                        content.append(f"*Proto-определения из: {endpoint['proto_repo']}*\n\n")
                    
                    if endpoint['request_json']:
                        content.append("**Запрос (JSON):**\n")
                        content.append("```json")
                        content.append(json.dumps(endpoint['request_json'], indent=2))
                        content.append("```\n\n")
                    
                    if endpoint['response_json']:
                        content.append("**Ответ (JSON):**\n")
                        content.append("```json")
                        content.append(json.dumps(endpoint['response_json'], indent=2))
                        content.append("```\n\n")
                    
                    file_link = self._create_file_link(endpoint['file'])
                    content.append(f"📍 *Определено в: {file_link}*\n\n")
        
        # REST endpoints grouped by file
        if api_spec.get('rest'):
            content.append("## REST эндпоинты\n\n")
            
            for file_path in sorted(files_rest.keys()):
                anchor = self._create_anchor_link(file_path)
                content.append(f"### {file_path}\n\n")
                content.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of endpoints
                endpoints_list = files_rest[file_path]
                content.append(f"<details open>\n<summary><b>Эндпоинты в этом файле ({len(endpoints_list)})</b></summary>\n\n")
                for endpoint in sorted(endpoints_list, key=lambda x: (x.get('method', ''), x.get('path', ''))):
                    method = endpoint['method']
                    path = endpoint['path']
                    endpoint_title = f"{method} {path}"
                    endpoint_anchor = self._create_anchor_link(endpoint_title)
                    content.append(f"- 🔗 [{endpoint_title}](#{endpoint_anchor})\n")
                content.append("\n</details>\n\n")
                
                # Endpoint details
                for endpoint in sorted(endpoints_list, key=lambda x: (x.get('method', ''), x.get('path', ''))):
                    method = endpoint['method']
                    path = endpoint['path']
                    content.append(f"#### {method} {path}\n\n")
                    
                    # Use existing comment or generate description
                    description = endpoint.get('comment', '').strip()
                    if not description:
                        description = generate_endpoint_description(
                            method=method,
                            path=path,
                            handler=endpoint.get('handler')
                        )
                    
                    if description:
                        content.append(f"{description}\n\n")
                    
                    content.append(f"**Handler:** `{endpoint['handler']}`\n")
                    content.append(f"**Router:** {endpoint['router']}\n\n")
                    
                    file_link = self._create_file_link(endpoint['file'])
                    content.append(f"📍 *Определено в: {file_link}*\n\n")
        
        if not api_spec.get('grpc') and not api_spec.get('rest'):
            content.append("API эндпоинты не найдены.\n")
        
        content.append("\n---\n\n")
        content.extend(self._sections_nav(current_depth=1))
        output_path = self.sections_dir / 'api.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_tests(self, tests: Dict):
        """Generate tests.md"""
        content = ["# Тестирование\n\n"]
        content.extend(self._sections_nav(current_depth=1))
        
        # Collect all files with tests
        files_tests: Dict[str, List[Dict]] = {}
        files_benchmarks: Dict[str, List[Dict]] = {}
        files_examples: Dict[str, List[Dict]] = {}
        
        if tests.get('tests'):
            for test in tests['tests']:
                file_path = test.get('file', '')
                files_tests.setdefault(file_path, []).append(test)
        
        if tests.get('benchmarks'):
            for bench in tests['benchmarks']:
                file_path = bench.get('file', '')
                files_benchmarks.setdefault(file_path, []).append(bench)
        
        if tests.get('examples'):
            for example in tests['examples']:
                file_path = example.get('file', '')
                files_examples.setdefault(file_path, []).append(example)
        
        all_files = sorted(set(list(files_tests.keys()) + list(files_benchmarks.keys()) + list(files_examples.keys())))
        
        # Menu by files
        if all_files:
            content.append("## Меню по файлам\n\n")
            for file_path in all_files:
                anchor = self._create_anchor_link(file_path)
                content.append(f"- 📄 [{file_path}](#{anchor})\n")
            content.append("\n---\n\n")
        
        # Tests grouped by file
        if tests.get('tests'):
            content.append("## Тесты\n\n")
            
            for file_path in sorted(files_tests.keys()):
                anchor = self._create_anchor_link(file_path)
                content.append(f"### {file_path}\n\n")
                content.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of tests
                tests_list = files_tests[file_path]
                content.append(f"<details open>\n<summary><b>Тесты в этом файле ({len(tests_list)})</b></summary>\n\n")
                for test in sorted(tests_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    test_name = test['name']
                    test_anchor = self._create_anchor_link(test_name)
                    line = test.get('line')
                    if line:
                        content.append(f"- 🔗 [{test_name}](#{test_anchor}) `:{line}`\n")
                    else:
                        content.append(f"- 🔗 [{test_name}](#{test_anchor})\n")
                content.append("\n</details>\n\n")
                
                # Test details
                for test in sorted(tests_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    content.append(f"#### {test['name']}\n\n")
                    if test['comment']:
                        content.append(f"{test['comment']}\n\n")
                    if test['subtests']:
                        content.append("**Сабтесты:**\n")
                        for subtest in test['subtests']:
                            content.append(f"- {subtest}\n")
                        content.append("\n")
                    file_link = self._create_file_link(test['file'], test.get('line'))
                    content.append(f"📍 *Расположение: {file_link}*\n\n")
        
        # Benchmarks grouped by file
        if tests.get('benchmarks'):
            content.append("## Бенчмарки\n\n")
            
            for file_path in sorted(files_benchmarks.keys()):
                anchor = self._create_anchor_link(file_path)
                content.append(f"### {file_path}\n\n")
                content.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of benchmarks
                benchmarks_list = files_benchmarks[file_path]
                content.append(f"<details open>\n<summary><b>Бенчмарки в этом файле ({len(benchmarks_list)})</b></summary>\n\n")
                for bench in sorted(benchmarks_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    bench_name = bench['name']
                    bench_anchor = self._create_anchor_link(bench_name)
                    line = bench.get('line')
                    if line:
                        content.append(f"- 🔗 [{bench_name}](#{bench_anchor}) `:{line}`\n")
                    else:
                        content.append(f"- 🔗 [{bench_name}](#{bench_anchor})\n")
                content.append("\n</details>\n\n")
                
                # Benchmark details
                for bench in sorted(benchmarks_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    content.append(f"#### {bench['name']}\n\n")
                    if bench['comment']:
                        content.append(f"{bench['comment']}\n\n")
                    file_link = self._create_file_link(bench['file'], bench.get('line'))
                    content.append(f"📍 *Расположение: {file_link}*\n\n")
        
        # Examples grouped by file
        if tests.get('examples'):
            content.append("## Примеры\n\n")
            
            for file_path in sorted(files_examples.keys()):
                anchor = self._create_anchor_link(file_path)
                content.append(f"### {file_path}\n\n")
                content.append(f"📄 Исходный файл: {self._create_file_link(file_path)}\n\n")
                
                # Expandable list of examples
                examples_list = files_examples[file_path]
                content.append(f"<details open>\n<summary><b>Примеры в этом файле ({len(examples_list)})</b></summary>\n\n")
                for example in sorted(examples_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    example_name = example['name']
                    example_anchor = self._create_anchor_link(example_name)
                    line = example.get('line')
                    if line:
                        content.append(f"- 🔗 [{example_name}](#{example_anchor}) `:{line}`\n")
                    else:
                        content.append(f"- 🔗 [{example_name}](#{example_anchor})\n")
                content.append("\n</details>\n\n")
                
                # Example details
                for example in sorted(examples_list, key=lambda x: (x.get('name', ''), x.get('line', 0))):
                    content.append(f"#### {example['name']}\n\n")
                    if example['comment']:
                        content.append(f"{example['comment']}\n\n")
                    file_link = self._create_file_link(example['file'], example.get('line'))
                    content.append(f"📍 *Расположение: {file_link}*\n\n")
        
        if not tests.get('tests') and not tests.get('benchmarks') and not tests.get('examples'):
            content.append("Тесты не найдены.\n")
        
        content.append("\n---\n\n")
        content.extend(self._sections_nav(current_depth=1))
        output_path = self.sections_dir / 'tests.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_libraries(self, libraries: Dict):
        """Generate libraries.md"""
        content = ["# Используемые библиотеки\n\n"]
        content.extend(self._sections_nav(current_depth=1))
        
        if libraries.get('module'):
            content.append(f"**Модуль:** `{libraries['module']}`\n\n")
        
        if libraries.get('dependencies'):
            content.append("## Зависимости\n\n")
            content.append("| Библиотека | Версия | Примечание |\n")
            content.append("|-----------|--------|------------|\n")
            
            for dep in sorted(libraries['dependencies'], key=lambda x: x['name']):
                name = dep['name']
                version = dep['version']
                comment = dep.get('comment', '')
                content.append(f"| `{name}` | `{version}` | {comment} |\n")
        
        if libraries.get('replace'):
            content.append("\n## Replace директивы\n\n")
            for replace in libraries['replace']:
                content.append(f"- `{replace['old']}` => `{replace.get('new', '')}`\n")
        
        if not libraries.get('dependencies'):
            content.append("Зависимости не найдены.\n")
        
        content.append("\n---\n\n")
        content.extend(self._sections_nav(current_depth=1))
        output_path = self.sections_dir / 'libraries.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_diagrams(self, component_info: Dict, api_spec: Dict):
        """Generate PlantUML diagrams"""
        components = component_info.get('components', {})
        
        if not components:
            return
        
        # Generate component dependency diagram
        component_diagram = self.plantuml_generator.generate_component_diagram(components)
        diagram_path = self.diagrams_dir / 'component_diagram.puml'
        diagram_path.write_text(component_diagram, encoding='utf-8')
        
        # Generate architecture diagram
        arch_diagram = self.plantuml_generator.generate_architecture_diagram(components, api_spec)
        arch_path = self.diagrams_dir / 'architecture_diagram.puml'
        arch_path.write_text(arch_diagram, encoding='utf-8')
        
        print(f"Generated PlantUML diagrams: {diagram_path}, {arch_path}")
    
    def _extract_section_titles(self, content: str) -> List[tuple]:
        """Extract all section titles (h1, h2) from markdown content."""
        titles = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                titles.append(('h1', title))
            elif line.startswith('## '):
                title = line[3:].strip()
                titles.append(('h2', title))
        return titles
    
    def _combine_sections(self, output_file: str, component_info: Dict = None):
        """Combine all documentation sections into README.md"""
        section_titles = []  # For navigation

        titles_ru = {
            "architecture_user": "Архитектура",
            "db_user": "Структура БД",
            "diagrams": "Диаграммы архитектуры",
            "imports": "Импорты",
            "structures": "Структуры и типы",
            "functions": "Функции",
            "api": "Спецификация API",
            "tests": "Тестирование",
            "libraries": "Используемые библиотеки",
            "others_user": "Прочее",
        }

        order = self.rules.get("readme_order") or [
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
        ]

        # User documentation directory: <go_repo>/docs/ (from source repository)
        user_dir = self.user_docs_dir

        def read_if_exists(p: Path) -> Optional[str]:
            try:
                return p.read_text(encoding="utf-8") if p.exists() else None
            except Exception:
                return None

        def add_section(name: str, content: str):
            readme_parts.append(content)
            readme_parts.append("\n---\n\n")

        readme_parts: List[str] = []
        readme_parts.append("# Документация сервиса\n")
        readme_parts.append("Документация автоматически сгенерирована из Go‑кода.\n\n")

        # Build sections content according to order and enabled flags
        sections_content: List[tuple] = []

        def menu_only(title: str, rel_path: str) -> Optional[str]:
            p = self.docs_dir / rel_path
            c = read_if_exists(p)
            if not c:
                return None
            # show only H2 menu (avoid huge output)
            h2 = []
            for level, t in self._extract_section_titles(c):
                if level != "h2":
                    continue
                if t.strip().lower() in {"меню", "menu"}:
                    continue
                h2.append(t)
            parts = [f"## {title}\n\n"]
            parts.append(f"- 📄 Подробнее: [{rel_path}]({rel_path})\n")
            if h2:
                parts.append("- 📚 Меню:\n")
                for t in h2:
                    parts.append(f"  - 🔗 [{t}]({rel_path}#{self._create_anchor_link(t)})\n")
            parts.append("\n")
            return "".join(parts)

        def user_section(title: str, filename: str) -> Optional[str]:
            """Read user-provided section from <go_repo>/docs/<filename>"""
            if not user_dir or not user_dir.exists():
                return None
            file_path = user_dir / filename
            content = read_if_exists(file_path)
            if not content:
                return None
            # Extract H2 titles for menu
            h2 = []
            for level, t in self._extract_section_titles(content):
                if level == "h2":
                    h2.append(t)
            parts = [f"## {title}\n\n"]
            if h2:
                parts.append("- 📚 Меню:\n")
                for t in h2:
                    parts.append(f"  - 🔗 [{t}](#{self._create_anchor_link(t)})\n")
                parts.append("\n---\n\n")
            parts.append(content)
            return "".join(parts)

        for key in order:
            if not is_enabled(self.rules, key):
                continue

            title = titles_ru.get(key, key)

            if key == "architecture_user":
                # Look in <go_repo>/docs/architecture.md
                c = user_section(title, "architecture.md")
                if c:
                    sections_content.append((title, c))
            elif key == "db_user":
                # Look in <go_repo>/docs/db.md
                c = user_section(title, "db.md")
                if c:
                    sections_content.append((title, c))
            elif key == "diagrams":
                if component_info and component_info.get("components"):
                    parts = [f"## {title}\n\n"]
                    parts.append("Диаграммы сохраняются в директорию `diagrams/`.\n\n")
                    parts.append("- 📄 Подробнее: [diagrams/](diagrams/)\n")
                    component_diagram_path = self.diagrams_dir / "component_diagram.puml"
                    if component_diagram_path.exists():
                        parts.append("- 🔗 [Зависимости компонентов](diagrams/component_diagram.puml)\n")
                    arch_diagram_path = self.diagrams_dir / "architecture_diagram.puml"
                    if arch_diagram_path.exists():
                        parts.append("- 🔗 [Архитектура сервиса](diagrams/architecture_diagram.puml)\n")
                    parts.append("\n")
                    sections_content.append((title, "".join(parts)))
            elif key == "imports":
                c = menu_only("Импорты", "sections/imports.md")
                if c:
                    sections_content.append(("Импорты", c))
            elif key == "structures":
                c = menu_only("Структуры и типы", "sections/structures.md")
                if c:
                    sections_content.append(("Структуры и типы", c))
            elif key == "functions":
                c = menu_only("Функции", "sections/functions.md")
                if c:
                    sections_content.append(("Функции", c))
            elif key == "api":
                c = menu_only("Спецификация API", "sections/api.md")
                if c:
                    sections_content.append(("Спецификация API", c))
            elif key == "tests":
                c = menu_only("Тестирование", "sections/tests.md")
                if c:
                    sections_content.append(("Тестирование", c))
            elif key == "libraries":
                c = menu_only("Используемые библиотеки", "sections/libraries.md")
                if c:
                    sections_content.append(("Используемые библиотеки", c))
            elif key == "others_user":
                # Look for other .md files in <go_repo>/docs/ (excluding architecture.md, db.md)
                if user_dir and user_dir.exists():
                    md_files = [
                        f
                        for f in user_dir.iterdir()
                        if f.is_file()
                        and f.suffix == ".md"
                        and f.name not in {"architecture.md", "db.md", "RULES.md"}
                    ]
                    if md_files:
                        parts = [f"## {title}\n\n"]
                        for f in sorted(md_files, key=lambda x: x.name):
                            fc = read_if_exists(f)
                            if not fc:
                                continue
                            parts.append(fc)
                            parts.append("\n")
                        sections_content.append((title, "\n".join(parts)))

        # Navigation
        # Extract titles after we have sections_content
        for sec_title, sec_content in sections_content:
            section_titles.append((sec_title, self._extract_section_titles(sec_content)))

        if section_titles:
            readme_parts.append("## Навигация\n\n")
            for section_name, titles in section_titles:
                if not titles:
                    continue
                main_anchor = self._create_anchor_link(section_name)
                readme_parts.append(f"- [{section_name}](#{main_anchor})\n")
                for level, t in titles:
                    if level == "h2":
                        # Avoid duplicate like "Импорты -> Импорты"
                        if self._create_anchor_link(t) == main_anchor:
                            continue
                        if t.strip().lower() in {"меню", "menu"}:
                            continue
                        anchor = self._create_anchor_link(t)
                        import re
                        clean_title = t
                        link_match = re.search(r"\[([^\]]+)\]", t)
                        if link_match:
                            clean_title = link_match.group(1)
                        readme_parts.append(f"  - [{clean_title}](#{anchor})\n")
            readme_parts.append("\n---\n\n")

        # Append sections in order
        for sec_title, sec_content in sections_content:
            add_section(sec_title, sec_content)

        readme_path = self.docs_dir / output_file
        readme_path.write_text("".join(readme_parts), encoding="utf-8")
