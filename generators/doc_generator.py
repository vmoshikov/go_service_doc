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


class DocumentationGenerator:
    def __init__(self, go_dir: Path, docs_dir: Path, user_docs_dir: Optional[Path] = None):
        self.go_dir = go_dir
        self.docs_dir = docs_dir
        self.user_docs_dir = user_docs_dir  # External user docs directory (from docs repo)
        self.structs = {}  # Will be set from API spec
        self.plantuml_generator = PlantUMLGenerator()
    
    def set_structs(self, structs: Dict):
        """Set struct definitions for JSON generation."""
        self.structs = structs
    
    def _create_file_link(self, file_path: str, line: Optional[int] = None) -> str:
        """Create a clickable link to a file with optional line number."""
        if line:
            # GitHub-style link: file.go#L123
            return f"[`{file_path}:{line}`]({file_path}#L{line})"
        else:
            return f"[`{file_path}`]({file_path})"
    
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
        output_file: str = 'README.md'
    ):
        """Generate complete documentation."""
        
        # Set structs for JSON generation
        self.structs = api_spec.get('structs', {})
        
        # Analyze components for diagrams
        print("Analyzing components and dependencies...")
        component_analyzer = ComponentAnalyzer(self.go_dir)
        component_info = component_analyzer.analyze()
        
        # Generate PlantUML diagrams
        self._generate_diagrams(component_info, api_spec)
        
        # Generate individual sections
        self._generate_functions(functions, api_spec)
        self._generate_api_spec(api_spec)
        self._generate_tests(tests)
        self._generate_libraries(libraries)
        
        # Combine all sections into README.md
        self._combine_sections(output_file, component_info)
    
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
        """Generate functions.md and directory-based README.md files."""
        if not functions:
            # Still create empty functions.md
            content = ["# Functions\n\nNo functions found.\n"]
            output_path = self.docs_dir / 'functions.md'
            output_path.write_text('\n'.join(content), encoding='utf-8')
            return
        
        # Group functions by directory
        functions_by_dir = {}
        for func in functions:
            file_path = Path(func['file'])
            # Get directory (relative to go_dir)
            dir_path = file_path.parent if file_path.parent != Path('.') else Path('')
            dir_key = str(dir_path) if dir_path else '.'
            
            if dir_key not in functions_by_dir:
                functions_by_dir[dir_key] = []
            functions_by_dir[dir_key].append(func)
        
        # Generate README.md for each directory
        directory_readmes = {}
        for dir_key, dir_funcs in sorted(functions_by_dir.items()):
            dir_readme = self._generate_directory_readme(dir_key, dir_funcs)
            directory_readmes[dir_key] = dir_readme
        
        # Generate parent functions.md with links to directories
        self._generate_parent_functions_md(functions_by_dir, directory_readmes)
    
    def _generate_directory_readme(self, dir_key: str, functions: List[Dict]) -> Dict:
        """Generate README.md for a specific directory."""
        content = []
        
        # Title based on directory
        if dir_key == '.':
            title = "# Root Functions\n"
            dir_display = "root"
        else:
            title = f"# Functions in `{dir_key}`\n"
            dir_display = dir_key
        
        content.append(title)
        content.append(f"This directory contains {len(functions)} function(s).\n\n")
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
                            content.append(f"**Request Type: `{struct_type}`**\n\n")
                            content.append("```json")
                            content.append(json.dumps(struct_json, indent=2))
                            content.append("```\n\n")
                    
                    # Response structs
                    for struct_type in struct_types.get('response', []):
                        struct_json = self._get_struct_json_for_type(struct_type)
                        if struct_json:
                            content.append(f"**Response Type: `{struct_type}`**\n\n")
                            content.append("```json")
                            content.append(json.dumps(struct_json, indent=2))
                            content.append("```\n\n")
                
                # Location link
                if dir_key == '.':
                    full_file_path = file_name
                else:
                    full_file_path = f"{dir_key}/{file_name}"
                file_link = self._create_file_link(full_file_path, func.get('line'))
                content.append(f"*Location: {file_link}*\n\n")
        
        # Write README.md to the directory
        if dir_key == '.':
            # For root directory, create in docs directory
            readme_path = self.docs_dir / 'functions_root.md'
        else:
            readme_path = self.go_dir / dir_key / 'README.md'
            readme_path.parent.mkdir(parents=True, exist_ok=True)
        
        readme_path.write_text('\n'.join(content), encoding='utf-8')
        
        # Return relative path from go_dir
        if dir_key == '.':
            rel_path = f"docs/functions_root.md"
        else:
            rel_path = str(readme_path.relative_to(self.go_dir))
        
        return {
            'path': rel_path,
            'dir': dir_display,
            'function_count': len(functions)
        }
    
    def _generate_parent_functions_md(self, functions_by_dir: Dict, directory_readmes: Dict):
        """Generate parent functions.md with links to directory READMEs."""
        content = ["# Functions\n"]
        content.append("Functions are organized by directory. Click on a directory to see detailed function documentation.\n\n")
        content.append("## Directory Index\n\n")
        
        for dir_key in sorted(functions_by_dir.keys()):
            dir_funcs = functions_by_dir[dir_key]
            dir_readme = directory_readmes.get(dir_key, {})
            
            if dir_key == '.':
                dir_display = "Root"
                readme_path = dir_readme.get('path', 'docs/functions_root.md')
            else:
                dir_display = dir_key
                readme_path = dir_readme.get('path', f"{dir_key}/README.md")
            
            func_count = len(dir_funcs)
            content.append(f"### {dir_display}\n")
            content.append(f"- **Functions:** {func_count}\n")
            content.append(f"- **Documentation:** [{readme_path}]({readme_path})\n\n")
            
            # List functions in this directory (group by name to avoid duplicates)
            content.append("**Functions:**\n")
            
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
        
        output_path = self.docs_dir / 'functions.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_api_spec(self, api_spec: Dict):
        """Generate api.md"""
        content = ["# API Specification\n"]
        
        # gRPC endpoints
        if api_spec.get('grpc'):
            content.append("## gRPC Endpoints\n\n")
            
            for endpoint in api_spec['grpc']:
                content.append(f"### {endpoint['method']}\n")
                
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
                request_display = f"**Request Type:** `{request_type}`"
                if endpoint.get('proto_link'):
                    proto_link = endpoint['proto_link']
                    request_display += f" - [View Proto Definition]({proto_link})"
                content.append(f"{request_display}\n")
                
                # Response type with external link if available
                response_type = endpoint.get('response_type', '')
                response_display = f"**Response Type:** `{response_type}`"
                if endpoint.get('proto_link'):
                    response_display += f" - [View Proto Definition]({proto_link})"
                content.append(f"{response_display}\n\n")
                
                # Add proto repository info if available
                if endpoint.get('proto_repo'):
                    content.append(f"*Proto definitions from: {endpoint['proto_repo']}*\n\n")
                
                if endpoint['request_json']:
                    content.append("**Request (JSON):**\n")
                    content.append("```json")
                    content.append(json.dumps(endpoint['request_json'], indent=2))
                    content.append("```\n\n")
                
                if endpoint['response_json']:
                    content.append("**Response (JSON):**\n")
                    content.append("```json")
                    content.append(json.dumps(endpoint['response_json'], indent=2))
                    content.append("```\n\n")
                
                file_link = self._create_file_link(endpoint['file'])
                content.append(f"*Defined in: {file_link}*\n\n")
        
        # REST endpoints
        if api_spec.get('rest'):
            content.append("## REST Endpoints\n\n")
            
            for endpoint in api_spec['rest']:
                method = endpoint['method']
                path = endpoint['path']
                
                content.append(f"### {method} {path}\n")
                
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
                content.append(f"*Defined in: {file_link}*\n\n")
        
        if not api_spec.get('grpc') and not api_spec.get('rest'):
            content.append("No API endpoints found.\n")
        
        output_path = self.docs_dir / 'api.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_tests(self, tests: Dict):
        """Generate test.md"""
        content = ["# Testing\n"]
        
        if tests.get('tests'):
            content.append("## Test Functions\n\n")
            for test in tests['tests']:
                content.append(f"### {test['name']}\n")
                if test['comment']:
                    content.append(f"{test['comment']}\n\n")
                if test['subtests']:
                    content.append("**Subtests:**\n")
                    for subtest in test['subtests']:
                        content.append(f"- {subtest}\n")
                file_link = self._create_file_link(test['file'], test.get('line'))
                content.append(f"*Location: {file_link}*\n\n")
        
        if tests.get('benchmarks'):
            content.append("## Benchmarks\n\n")
            for bench in tests['benchmarks']:
                content.append(f"### {bench['name']}\n")
                if bench['comment']:
                    content.append(f"{bench['comment']}\n\n")
                file_link = self._create_file_link(bench['file'], bench.get('line'))
                content.append(f"*Location: {file_link}*\n\n")
        
        if tests.get('examples'):
            content.append("## Examples\n\n")
            for example in tests['examples']:
                content.append(f"### {example['name']}\n")
                if example['comment']:
                    content.append(f"{example['comment']}\n\n")
                file_link = self._create_file_link(example['file'], example.get('line'))
                content.append(f"*Location: {file_link}*\n\n")
        
        if not tests.get('tests') and not tests.get('benchmarks') and not tests.get('examples'):
            content.append("No tests found.\n")
        
        output_path = self.docs_dir / 'test.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_libraries(self, libraries: Dict):
        """Generate libraries.md"""
        content = ["# Libraries Used\n"]
        
        if libraries.get('module'):
            content.append(f"**Module:** `{libraries['module']}`\n\n")
        
        if libraries.get('dependencies'):
            content.append("## Dependencies\n\n")
            content.append("| Library | Version | Notes |\n")
            content.append("|---------|---------|-------|\n")
            
            for dep in sorted(libraries['dependencies'], key=lambda x: x['name']):
                name = dep['name']
                version = dep['version']
                comment = dep.get('comment', '')
                content.append(f"| `{name}` | `{version}` | {comment} |\n")
        
        if libraries.get('replace'):
            content.append("\n## Replace Directives\n\n")
            for replace in libraries['replace']:
                content.append(f"- `{replace['old']}` => `{replace.get('new', '')}`\n")
        
        if not libraries.get('dependencies'):
            content.append("No dependencies found.\n")
        
        output_path = self.docs_dir / 'libraries.md'
        output_path.write_text('\n'.join(content), encoding='utf-8')
    
    def _generate_diagrams(self, component_info: Dict, api_spec: Dict):
        """Generate PlantUML diagrams"""
        components = component_info.get('components', {})
        
        if not components:
            return
        
        # Generate component dependency diagram
        component_diagram = self.plantuml_generator.generate_component_diagram(components)
        diagram_path = self.docs_dir / 'component_diagram.puml'
        diagram_path.write_text(component_diagram, encoding='utf-8')
        
        # Generate architecture diagram
        arch_diagram = self.plantuml_generator.generate_architecture_diagram(components, api_spec)
        arch_path = self.docs_dir / 'architecture_diagram.puml'
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
        sections = []
        section_titles = []  # For navigation
        
        # User-provided sections (optional)
        # First check external user docs directory (from docs repo)
        user_docs_source = self.user_docs_dir if self.user_docs_dir else self.docs_dir
        
        user_sections = [
            ('user_architecture.md', 'Architecture'),
            ('user_db_structure.md', 'DB Structure'),
        ]
        
        # Auto-generated sections
        auto_sections = [
            ('functions.md', 'Functions'),
            ('api.md', 'API Specification'),
            ('test.md', 'Testing'),
            ('libraries.md', 'Libraries Used'),
        ]
        
        # Add user sections first (from external docs or local)
        for filename, title in user_sections:
            # Try external user docs first
            file_path = None
            if self.user_docs_dir and self.user_docs_dir.exists():
                file_path = self.user_docs_dir / filename
                if not file_path.exists():
                    file_path = None
            
            # Fallback to local docs
            if not file_path:
                file_path = self.docs_dir / filename
            
            if file_path.exists():
                content = file_path.read_text(encoding='utf-8')
                sections.append((title, content))
                # Extract titles for navigation
                titles = self._extract_section_titles(content)
                section_titles.append((title, titles))
        
        # Add auto-generated sections
        for filename, title in auto_sections:
            file_path = self.docs_dir / filename
            if file_path.exists():
                content = file_path.read_text(encoding='utf-8')
                sections.append((title, content))
                # Extract titles for navigation
                titles = self._extract_section_titles(content)
                section_titles.append((title, titles))
        
        # Check for other user files (from external docs or local)
        other_files = []
        
        # Check external user docs directory
        if self.user_docs_dir and self.user_docs_dir.exists():
            other_files.extend([
                f for f in self.user_docs_dir.iterdir()
                if f.is_file() and f.suffix == '.md' and f.name not in [
                    'user_architecture.md', 'user_db_structure.md',
                    'functions.md', 'api.md', 'test.md', 'libraries.md'
                ]
            ])
        
        # Check local docs directory
        if self.docs_dir.exists():
            other_files.extend([
                f for f in self.docs_dir.iterdir()
                if f.is_file() and f.suffix == '.md' and f.name not in [
                    'user_architecture.md', 'user_db_structure.md',
                    'functions.md', 'api.md', 'test.md', 'libraries.md'
                ]
            ])
        
        # Remove duplicates
        seen = set()
        unique_files = []
        for f in other_files:
            if f.name not in seen:
                seen.add(f.name)
                unique_files.append(f)
        
        if unique_files:
            sections.append(('Others', ''))
            for other_file in sorted(unique_files, key=lambda x: x.name):
                content = other_file.read_text(encoding='utf-8')
                sections.append((other_file.stem, content))
                titles = self._extract_section_titles(content)
                section_titles.append((other_file.stem, titles))
        
        # Combine into README
        readme_content = []
        readme_content.append("# Service Documentation\n")
        readme_content.append("This documentation is automatically generated from the Go service codebase.\n\n")
        
        # Add Architecture Diagrams section
        if component_info and component_info.get('components'):
            readme_content.append("## Architecture Diagrams\n\n")
            
            # Component Dependencies Diagram
            component_diagram_path = self.docs_dir / 'component_diagram.puml'
            if component_diagram_path.exists():
                readme_content.append("### Component Dependencies\n\n")
                readme_content.append("```plantuml")
                readme_content.append(component_diagram_path.read_text(encoding='utf-8'))
                readme_content.append("```\n\n")
                readme_content.append("*To render this diagram, use a PlantUML renderer or view it in your IDE/editor with PlantUML support.*\n\n")
            
            # Architecture Diagram
            arch_diagram_path = self.docs_dir / 'architecture_diagram.puml'
            if arch_diagram_path.exists():
                readme_content.append("### Service Architecture\n\n")
                readme_content.append("```plantuml")
                readme_content.append(arch_diagram_path.read_text(encoding='utf-8'))
                readme_content.append("```\n\n")
                readme_content.append("*To render this diagram, use a PlantUML renderer or view it in your IDE/editor with PlantUML support.*\n\n")
            
            readme_content.append("---\n\n")
        
        # Add Navigation section
        if section_titles:
            readme_content.append("## Navigation\n\n")
            for section_name, titles in section_titles:
                if not titles:
                    continue
                # Main section link
                main_anchor = self._create_anchor_link(section_name)
                readme_content.append(f"- [{section_name}](#{main_anchor})\n")
                
                # Sub-sections (h2 only, to avoid too much nesting)
                for level, title in titles:
                    if level == 'h2':
                        anchor = self._create_anchor_link(title)
                        # Clean title (remove markdown links)
                        clean_title = title
                        # Extract text from markdown links
                        import re
                        link_match = re.search(r'\[([^\]]+)\]', title)
                        if link_match:
                            clean_title = link_match.group(1)
                        readme_content.append(f"  - [{clean_title}](#{anchor})\n")
            
            readme_content.append("\n---\n\n")
        
        # Add Functions section with directory links (if exists)
        functions_md_path = self.docs_dir / 'functions.md'
        if functions_md_path.exists():
            functions_content = functions_md_path.read_text(encoding='utf-8')
            readme_content.append(functions_content)
            readme_content.append("\n---\n\n")
        
        # Add other sections (skip Functions as we already added it)
        for title, content in sections:
            if title == 'Others' and not content:
                continue
            if title == 'Functions':
                # Skip functions as we already added it above
                continue
            readme_content.append(content)
            readme_content.append("\n---\n\n")
        
        # Write README.md to the Go service directory
        readme_path = self.go_dir / output_file
        readme_path.write_text('\n'.join(readme_content), encoding='utf-8')
