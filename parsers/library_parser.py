"""
Library Parser for Go code

Extracts dependencies from go.mod file.
"""

import re
from pathlib import Path
from typing import Dict


class LibraryParser:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
    
    def parse(self) -> Dict:
        """Parse go.mod file to extract dependencies."""
        go_mod_path = self.go_dir / 'go.mod'
        
        if not go_mod_path.exists():
            print(f"Warning: go.mod not found at {go_mod_path}")
            return {'module': 'unknown', 'dependencies': [], 'replace': []}
        
        try:
            content = go_mod_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read go.mod: {e}")
            return {'module': 'unknown', 'dependencies': [], 'replace': []}
        
        libraries = []
        
        # Parse module name
        module_match = re.search(r'^module\s+(\S+)', content, re.MULTILINE)
        module_name = module_match.group(1) if module_match else 'unknown'
        
        # Parse require statements
        require_pattern = re.compile(
            r'^\s*(\S+)\s+(\S+)(?:\s+//\s*(.+))?$',
            re.MULTILINE
        )
        
        in_require_block = False
        for line in content.split('\n'):
            line = line.strip()
            
            if line == 'require (':
                in_require_block = True
                continue
            elif line == ')' and in_require_block:
                in_require_block = False
                continue
            elif line.startswith('require '):
                # Single line require
                match = re.match(r'require\s+(\S+)\s+(\S+)(?:\s+//\s*(.+))?', line)
                if match:
                    libraries.append({
                        'name': match.group(1),
                        'version': match.group(2),
                        'comment': match.group(3) if match.group(3) else ''
                    })
            elif in_require_block or line.startswith(('require ', '\t')):
                # In require block or indented require
                match = require_pattern.match(line)
                if match:
                    libraries.append({
                        'name': match.group(1),
                        'version': match.group(2),
                        'comment': match.group(3) if match.group(3) else ''
                    })
        
        # Also check for replace and exclude directives
        replace_directives = []
        replace_pattern = re.compile(
            r'^replace\s+(\S+)(?:\s+=>\s+(\S+))?(?:\s+(\S+))?',
            re.MULTILINE
        )
        for match in replace_pattern.finditer(content):
            replace_directives.append({
                'old': match.group(1),
                'new': match.group(2) or match.group(3) or ''
            })
        
        return {
            'module': module_name,
            'dependencies': libraries,
            'replace': replace_directives
        }
