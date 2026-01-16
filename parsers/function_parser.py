"""
Function Parser for Go code

Extracts function definitions, their signatures, and comments from Go source files.
Uses tree-sitter for accurate parsing, falls back to regex if unavailable.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

from parsers.tree_sitter_helper import TreeSitterGoParser


class FunctionParser:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.ts_parser = TreeSitterGoParser()
        self.use_tree_sitter = self.ts_parser.is_available()
        self.structs = {}  # Will be populated from API parser
    
    def set_structs(self, structs: Dict):
        """Set struct definitions from API parser."""
        self.structs = structs
    
    def _extract_struct_types(self, params: str, returns: str) -> Dict:
        """Extract struct types from function parameters and return types."""
        struct_types = {
            'request': [],
            'response': []
        }
        
        # Extract struct types from parameters
        if params:
            # Pattern to match struct types: *TypeName or TypeName
            param_pattern = re.compile(r'\*\s*([a-zA-Z_][a-zA-Z0-9_.]*)\s*\w*')
            for match in param_pattern.finditer(params):
                type_name = match.group(1)
                # Check if it's a struct type (not basic types)
                if not self._is_basic_type(type_name):
                    struct_types['request'].append(type_name)
        
        # Extract struct types from return types
        if returns:
            return_pattern = re.compile(r'\*\s*([a-zA-Z_][a-zA-Z0-9_.]*)|([a-zA-Z_][a-zA-Z0-9_.]*)')
            for match in return_pattern.finditer(returns):
                type_name = match.group(1) or match.group(2)
                if type_name and not self._is_basic_type(type_name):
                    struct_types['response'].append(type_name)
        
        return struct_types
    
    def _is_basic_type(self, type_name: str) -> bool:
        """Check if a type is a basic Go type."""
        basic_types = {
            'string', 'int', 'int8', 'int16', 'int32', 'int64',
            'uint', 'uint8', 'uint16', 'uint32', 'uint64',
            'float32', 'float64', 'bool', 'byte', 'rune',
            'error', 'context', 'Context'
        }
        return type_name in basic_types or type_name.startswith('[]') or type_name.startswith('map[')
    
    def parse(self) -> List[Dict]:
        """Parse all Go functions from the codebase."""
        functions = []
        
        # Find all .go files (excluding test files and vendor)
        go_files = list(self.go_dir.rglob('*.go'))
        go_files = [
            f for f in go_files
            if not f.name.endswith('_test.go') and 'vendor' not in str(f)
        ]
        
        for go_file in go_files:
            file_functions = self._parse_file(go_file)
            functions.extend(file_functions)
        
        return functions
    
    def _parse_file(self, file_path: Path) -> List[Dict]:
        """Parse functions from a single Go file."""
        if self.use_tree_sitter:
            return self._parse_file_tree_sitter(file_path)
        else:
            return self._parse_file_regex(file_path)
    
    def _parse_file_tree_sitter(self, file_path: Path) -> List[Dict]:
        """Parse functions using tree-sitter."""
        functions = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            source_bytes = bytes(content, 'utf-8')
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return functions
        
        tree = self.ts_parser.parse_file(file_path)
        if not tree:
            # Fallback to regex if tree-sitter parsing fails
            return self._parse_file_regex(file_path)
        
        # Find all function declarations
        func_nodes = self.ts_parser.find_nodes_by_type(tree, 'method_declaration')
        func_nodes.extend(self.ts_parser.find_nodes_by_type(tree, 'function_declaration'))
        
        for func_node in func_nodes:
            sig = self.ts_parser.extract_function_signature(func_node, source_bytes)
            
            # Extract params and returns more accurately from AST
            params = sig['params']
            returns = sig['returns']
            receiver = sig['receiver']
            
            # For method_declaration, the structure is: receiver, name, parameters, result
            # For function_declaration, the structure is: name, parameters, result
            is_method = func_node.type == 'method_declaration'
            
            # More accurate extraction
            name_found = False
            receiver_found = False
            for child in func_node.children:
                if child.type in ['field_identifier', 'identifier']:
                    if not name_found:
                        sig['name'] = self.ts_parser.get_node_text(child, source_bytes)
                        name_found = True
                elif child.type == 'parameter_list':
                    if is_method and not receiver_found:
                        receiver = self.ts_parser.get_node_text(child, source_bytes)
                        receiver_found = True
                    elif name_found or not is_method:
                        params = self.ts_parser.get_node_text(child, source_bytes)
                elif child.type == 'type_identifier':
                    # Could be return type, but result node is better
                    pass
            
            # Look for result node (return type)
            # In Go AST, result comes after parameters
            for child in func_node.children:
                if child.type in ['type_identifier', 'pointer_type', 'slice_type', 
                                 'array_type', 'map_type', 'function_type', 
                                 'qualified_type', 'parameter_list']:
                    # Check if this is after parameters (result)
                    if name_found and params:
                        # This might be the return type
                        node_text = self.ts_parser.get_node_text(child, source_bytes)
                        # If it's a parameter_list after params, it's multiple returns
                        if child.type == 'parameter_list' and child.start_point[1] > 0:
                            returns = node_text
                        elif child.type != 'parameter_list' and not returns:
                            returns = node_text
            
            if not sig['name']:
                continue
            
            # Extract struct types
            struct_types = self._extract_struct_types(params, returns)
            
            functions.append({
                'name': sig['name'],
                'receiver': receiver,
                'params': params,
                'returns': returns,
                'comment': sig['comment'],
                'struct_types': struct_types,
                'file': str(file_path.relative_to(self.go_dir)),
                'line': func_node.start_point[0] + 1
            })
        
        return functions
    
    def _parse_file_regex(self, file_path: Path) -> List[Dict]:
        """Parse functions using regex (fallback)."""
        functions = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return functions
        
        # More comprehensive pattern
        func_pattern_v2 = re.compile(
            r'(?:^|\n)(?P<comment>(?:^\s*//.*\n)*)'  # Comments
            r'\s*func\s+'
            r'(?P<receiver>\([^)]+\)\s+)?'  # Optional receiver
            r'(?P<name>\w+)'  # Function name
            r'\s*\((?P<params>[^)]*)\)'  # Parameters
            r'\s*(?P<returns>\([^)]*\)|[\w\[\]*\s]+)?'  # Return type
            r'\s*\{',
            re.MULTILINE
        )
        
        matches = list(func_pattern_v2.finditer(content))
        
        for match in matches:
            comment = match.group('comment') or ''
            receiver = match.group('receiver') or ''
            name = match.group('name')
            params = match.group('params') or ''
            returns = match.group('returns') or ''
            
            # Clean up comment
            comment_lines = [
                line.strip().lstrip('//').strip()
                for line in comment.split('\n')
                if line.strip().startswith('//')
            ]
            comment_text = ' '.join(comment_lines)
            
            # Get function location
            start_pos = match.start()
            line_num = content[:start_pos].count('\n') + 1
            
            # Extract struct types
            struct_types = self._extract_struct_types(params.strip(), returns.strip())
            
            functions.append({
                'name': name,
                'receiver': receiver.strip() if receiver else None,
                'params': params.strip(),
                'returns': returns.strip(),
                'comment': comment_text,
                'struct_types': struct_types,
                'file': str(file_path.relative_to(self.go_dir)),
                'line': line_num
            })
        
        return functions
