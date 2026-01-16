"""
Component Analyzer

Analyzes Go codebase to detect components, packages, and their dependencies.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict

from parsers.tree_sitter_helper import TreeSitterGoParser


class ComponentAnalyzer:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.ts_parser = TreeSitterGoParser()
        self.use_tree_sitter = self.ts_parser.is_available()
        self.components = {}
        self.dependencies = defaultdict(set)
        self.packages = set()
    
    def analyze(self) -> Dict:
        """Analyze codebase to extract components and dependencies"""
        go_files = list(self.go_dir.rglob('*.go'))
        go_files = [
            f for f in go_files
            if not f.name.endswith('_test.go') and 'vendor' not in str(f)
        ]
        
        # Extract package information and imports
        for go_file in go_files:
            self._analyze_file(go_file)
        
        # Build component graph
        components = self._build_component_graph()
        
        return {
            'components': components,
            'dependencies': dict(self.dependencies),
            'packages': sorted(self.packages)
        }
    
    def _analyze_file(self, file_path: Path):
        """Analyze a single Go file for packages and imports"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            return
        
        # Extract package name
        package_match = re.search(r'^package\s+(\w+)', content, re.MULTILINE)
        if package_match:
            package_name = package_match.group(1)
            self.packages.add(package_name)
            
            # Get directory as component name
            rel_path = file_path.relative_to(self.go_dir)
            component = str(rel_path.parent) if rel_path.parent != Path('.') else 'root'
            
            if component not in self.components:
                self.components[component] = {
                    'name': component,
                    'package': package_name,
                    'files': []
                }
            
            self.components[component]['files'].append(str(rel_path))
        
        # Extract imports
        import_pattern = re.compile(
            r'^import\s+(?:(?:\()|(?:"([^"]+)"|`([^`]+)`)|(\w+\s+"([^"]+)"))',
            re.MULTILINE
        )
        
        # More comprehensive import extraction
        imports = self._extract_imports(content)
        
        # Get component for this file
        rel_path = file_path.relative_to(self.go_dir)
        source_component = str(rel_path.parent) if rel_path.parent != Path('.') else 'root'
        
        # Track dependencies
        for imp in imports:
            # Skip standard library
            if not imp.startswith('github.com') and not imp.startswith('golang.org') and not '/' in imp:
                continue
            
            # Extract package name from import
            target_package = imp.split('/')[-1]
            
            # Find which component this import belongs to
            target_component = self._find_component_for_import(imp)
            
            if target_component and target_component != source_component:
                self.dependencies[source_component].add(target_component)
    
    def _extract_imports(self, content: str) -> List[str]:
        """Extract all import statements from Go file"""
        imports = []
        
        # Pattern for single import
        single_import = re.compile(r'^import\s+"([^"]+)"', re.MULTILINE)
        
        # Pattern for import block
        import_block = re.compile(
            r'^import\s*\(([^)]+)\)',
            re.MULTILINE | re.DOTALL
        )
        
        # Check for import block first
        block_match = import_block.search(content)
        if block_match:
            block_content = block_match.group(1)
            for line in block_content.split('\n'):
                line = line.strip()
                if line.startswith('"') or line.startswith('_') or line.startswith('.'):
                    # Extract import path
                    match = re.search(r'"([^"]+)"', line)
                    if match:
                        imports.append(match.group(1))
        else:
            # Single import
            match = single_import.search(content)
            if match:
                imports.append(match.group(1))
        
        return imports
    
    def _find_component_for_import(self, import_path: str) -> Optional[str]:
        """Find which component/package an import belongs to"""
        # Check if it's a local import (starts with ./ or ../)
        if import_path.startswith('./') or import_path.startswith('../'):
            return None  # Relative imports within same component
        
        # Check if it's an external package (starts with domain)
        if '/' in import_path:
            # External package - check if it's in our codebase
            parts = import_path.split('/')
            # Try to find matching directory
            for component, info in self.components.items():
                if info['package'] == parts[-1]:
                    return component
        
        return None
    
    def _build_component_graph(self) -> Dict:
        """Build component dependency graph"""
        components = {}
        
        for component_name, component_info in self.components.items():
            deps = list(self.dependencies.get(component_name, set()))
            components[component_name] = {
                'name': component_name,
                'package': component_info['package'],
                'files': component_info['files'],
                'dependencies': deps,
                'dependents': []
            }
        
        # Build reverse dependencies (dependents)
        for component_name, deps in self.dependencies.items():
            for dep in deps:
                if dep in components:
                    components[dep]['dependents'].append(component_name)
        
        return components
