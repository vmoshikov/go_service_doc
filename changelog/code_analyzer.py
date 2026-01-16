"""
Code Analyzer

Analyzes code changes using tree-sitter to understand what was added/changed/removed.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

from changelog.git_analyzer import GitAnalyzer
from parsers.tree_sitter_helper import TreeSitterGoParser


class CodeAnalyzer:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.git_analyzer = GitAnalyzer(go_dir)
        self.ts_parser = TreeSitterGoParser()
    
    def analyze_changes(self, commits: List[Dict]) -> Dict[str, List[Dict]]:
        """Analyze code changes and categorize them"""
        changes = {
            'added': [],
            'changed': [],
            'deprecated': [],
            'removed': [],
            'fixed': [],
            'security': []
        }
        
        for commit in commits:
            commit_hash = commit['hash']
            changed_files = self.git_analyzer.get_changed_files(commit_hash)
            
            # Filter Go files
            go_files = [f for f in changed_files if f.endswith('.go') and 'vendor' not in f]
            
            for file_path in go_files:
                diff = self.git_analyzer.get_file_diff(commit_hash, file_path)
                file_changes = self._analyze_file_changes(file_path, diff, commit)
                
                # Categorize changes
                for change in file_changes:
                    change_type = self._categorize_change(change, commit)
                    if change_type:
                        changes[change_type].append(change)
        
        return changes
    
    def _analyze_file_changes(self, file_path: str, diff: str, commit: Dict) -> List[Dict]:
        """Analyze changes in a single file"""
        changes = []
        
        # Parse diff to find added/removed functions
        added_functions = self._extract_added_functions(diff)
        removed_functions = self._extract_removed_functions(diff)
        changed_functions = self._extract_changed_functions(diff)
        
        for func_name in added_functions:
            changes.append({
                'type': 'function',
                'name': func_name,
                'action': 'added',
                'file': file_path,
                'commit': commit['hash'],
                'message': commit['subject']
            })
        
        for func_name in removed_functions:
            changes.append({
                'type': 'function',
                'name': func_name,
                'action': 'removed',
                'file': file_path,
                'commit': commit['hash'],
                'message': commit['subject']
            })
        
        for func_name in changed_functions:
            changes.append({
                'type': 'function',
                'name': func_name,
                'action': 'changed',
                'file': file_path,
                'commit': commit['hash'],
                'message': commit['subject']
            })
        
        # Check for API endpoint changes
        api_changes = self._extract_api_changes(diff)
        changes.extend(api_changes)
        
        return changes
    
    def _extract_added_functions(self, diff: str) -> List[str]:
        """Extract function names from added lines"""
        functions = []
        
        # Pattern for function definitions in added lines
        pattern = r'^\+\s*func\s+(?:\([^)]+\)\s+)?(\w+)\s*\('
        
        for line in diff.split('\n'):
            if line.startswith('+') and not line.startswith('+++'):
                match = re.search(pattern, line)
                if match:
                    functions.append(match.group(1))
        
        return functions
    
    def _extract_removed_functions(self, diff: str) -> List[str]:
        """Extract function names from removed lines"""
        functions = []
        
        # Pattern for function definitions in removed lines
        pattern = r'^-\s*func\s+(?:\([^)]+\)\s+)?(\w+)\s*\('
        
        for line in diff.split('\n'):
            if line.startswith('-') and not line.startswith('---'):
                match = re.search(pattern, line)
                if match:
                    functions.append(match.group(1))
        
        return functions
    
    def _extract_changed_functions(self, diff: str) -> List[str]:
        """Extract function names that were modified"""
        functions = []
        
        # Look for functions that have both + and - lines
        added_funcs = set(self._extract_added_functions(diff))
        removed_funcs = set(self._extract_removed_functions(diff))
        
        # Functions that appear in both are likely changed
        changed = added_funcs & removed_funcs
        
        return list(changed)
    
    def _extract_api_changes(self, diff: str) -> List[Dict]:
        """Extract API endpoint changes"""
        changes = []
        
        # Patterns for common API router registrations
        patterns = [
            (r'router\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*"([^"]+)"', 'rest'),
            (r'e\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*"([^"]+)"', 'rest'),
            (r'http\.HandleFunc\s*\(\s*"([^"]+)"', 'rest'),
        ]
        
        for line in diff.split('\n'):
            if line.startswith('+') or line.startswith('-'):
                for pattern, api_type in patterns:
                    match = re.search(pattern, line)
                    if match:
                        if api_type == 'rest':
                            method = match.group(1) if len(match.groups()) > 1 else 'GET'
                            path = match.group(2) if len(match.groups()) > 1 else match.group(1)
                            
                            action = 'added' if line.startswith('+') else 'removed'
                            changes.append({
                                'type': 'api',
                                'api_type': 'rest',
                                'method': method,
                                'path': path,
                                'action': action,
                                'commit': '',
                                'message': ''
                            })
        
        return changes
    
    def _categorize_change(self, change: Dict, commit: Dict) -> Optional[str]:
        """Categorize change based on commit message and change type"""
        message = commit.get('subject', '').lower()
        body = commit.get('body', '').lower()
        full_message = f"{message} {body}".lower()
        
        # Security fixes
        if any(word in full_message for word in ['security', 'vulnerability', 'cve', 'exploit']):
            return 'security'
        
        # Bug fixes
        if any(word in full_message for word in ['fix', 'bug', 'error', 'issue', 'problem']):
            return 'fixed'
        
        # Removals
        if change.get('action') == 'removed':
            return 'removed'
        
        # Deprecations
        if any(word in full_message for word in ['deprecate', 'obsolete', 'remove in']):
            return 'deprecated'
        
        # Additions
        if change.get('action') == 'added':
            return 'added'
        
        # Changes
        if change.get('action') == 'changed':
            return 'changed'
        
        # Default to added for new things
        return 'added'
