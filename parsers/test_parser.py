"""
Test Parser for Go code

Extracts test functions and test cases from Go test files.
Uses tree-sitter for accurate parsing, falls back to regex if unavailable.
"""

import re
from pathlib import Path
from typing import Dict, List

from parsers.tree_sitter_helper import TreeSitterGoParser


class TestParser:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.ts_parser = TreeSitterGoParser()
        self.use_tree_sitter = self.ts_parser.is_available()
    
    def parse(self) -> Dict:
        """Parse all test files from the codebase."""
        test_files = list(self.go_dir.rglob('*_test.go'))
        test_files = [f for f in test_files if 'vendor' not in str(f)]
        
        tests = []
        benchmarks = []
        examples = []
        
        for test_file in test_files:
            file_tests = self._parse_test_file(test_file)
            
            for test in file_tests:
                if test['type'] == 'test':
                    tests.append(test)
                elif test['type'] == 'benchmark':
                    benchmarks.append(test)
                elif test['type'] == 'example':
                    examples.append(test)
        
        return {
            'tests': tests,
            'benchmarks': benchmarks,
            'examples': examples
        }
    
    def _parse_test_file(self, test_file: Path) -> List[Dict]:
        """Parse a single test file."""
        if self.use_tree_sitter:
            return self._parse_test_file_tree_sitter(test_file)
        else:
            return self._parse_test_file_regex(test_file)
    
    def _parse_test_file_tree_sitter(self, test_file: Path) -> List[Dict]:
        """Parse test file using tree-sitter."""
        tests = []
        
        try:
            content = test_file.read_text(encoding='utf-8')
            source_bytes = bytes(content, 'utf-8')
        except Exception as e:
            print(f"Warning: Could not read {test_file}: {e}")
            return tests
        
        tree = self.ts_parser.parse_file(test_file)
        if not tree:
            # Fallback to regex
            return self._parse_test_file_regex(test_file)
        
        # Find all function declarations
        func_nodes = self.ts_parser.find_nodes_by_type(tree, 'function_declaration')
        
        for func_node in func_nodes:
            # Get function name
            func_name = None
            for child in func_node.children:
                if child.type == 'identifier':
                    func_name = self.ts_parser.get_node_text(child, source_bytes)
                    break
            
            if not func_name:
                continue
            
            # Check if it's a test function
            if not (func_name.startswith('Test') or 
                   func_name.startswith('Benchmark') or 
                   func_name.startswith('Example')):
                continue
            
            # Determine test type
            if func_name.startswith('Test'):
                test_type = 'test'
            elif func_name.startswith('Benchmark'):
                test_type = 'benchmark'
            elif func_name.startswith('Example'):
                test_type = 'example'
            else:
                continue
            
            # Get comment
            comment = self.ts_parser.get_comment_before_node(func_node, source_bytes)
            
            # Extract subtests (t.Run calls) - use regex for this
            func_body = self.ts_parser.get_node_text(func_node, source_bytes)
            subtest_pattern = re.compile(
                r'\.Run\s*\(\s*"([^"]+)"\s*,\s*func',
                re.MULTILINE
            )
            subtests = subtest_pattern.findall(func_body)
            
            tests.append({
                'type': test_type,
                'name': func_name,
                'comment': comment,
                'subtests': subtests,
                'file': str(test_file.relative_to(self.go_dir)),
                'line': func_node.start_point[0] + 1
            })
        
        return tests
    
    def _parse_test_file_regex(self, test_file: Path) -> List[Dict]:
        """Parse test file using regex (fallback)."""
        tests = []
        
        try:
            content = test_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read {test_file}: {e}")
            return tests
        
        # Pattern for test functions: func TestXxx(t *testing.T)
        test_pattern = re.compile(
            r'(?:^|\n)(?P<comment>(?:^\s*//.*\n)*)'
            r'\s*func\s+'
            r'(?P<name>Test\w+|Benchmark\w+|Example\w+)'
            r'\s*\([^)]+\)\s*\{',
            re.MULTILINE
        )
        
        matches = test_pattern.finditer(content)
        
        for match in matches:
            comment = match.group('comment') or ''
            name = match.group('name')
            
            # Determine test type
            if name.startswith('Test'):
                test_type = 'test'
            elif name.startswith('Benchmark'):
                test_type = 'benchmark'
            elif name.startswith('Example'):
                test_type = 'example'
            else:
                continue
            
            # Clean comment
            comment_lines = [
                line.strip().lstrip('//').strip()
                for line in comment.split('\n')
                if line.strip().startswith('//')
            ]
            comment_text = '\n'.join(comment_lines)
            
            # Extract subtests (t.Run calls)
            subtest_pattern = re.compile(
                rf'\.Run\s*\(\s*"([^"]+)"\s*,\s*func',
                re.MULTILINE
            )
            start_pos = match.end()
            # Find the end of the function (simplified - find matching brace)
            func_body = self._extract_function_body(content, start_pos)
            subtests = subtest_pattern.findall(func_body)
            
            # Get line number
            line_num = content[:match.start()].count('\n') + 1
            
            tests.append({
                'type': test_type,
                'name': name,
                'comment': comment_text,
                'subtests': subtests,
                'file': str(test_file.relative_to(self.go_dir)),
                'line': line_num
            })
        
        return tests
    
    def _extract_function_body(self, content: str, start_pos: int) -> str:
        """Extract function body by matching braces."""
        brace_count = 1
        pos = start_pos
        end_pos = start_pos
        
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
            pos += 1
        
        if brace_count == 0:
            end_pos = pos
        
        return content[start_pos:end_pos]
