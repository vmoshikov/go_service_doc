"""
Tree-sitter helper for Go code parsing

Provides utilities for parsing Go code using tree-sitter.
"""

from pathlib import Path
from typing import Optional, Dict, List
import tree_sitter
from tree_sitter import Language, Parser


class TreeSitterGoParser:
    """Helper class for parsing Go code with tree-sitter."""
    
    def __init__(self):
        self.parser = None
        self.language = None
        self._initialize_parser()
    
    def _initialize_parser(self):
        """Initialize tree-sitter parser for Go."""
        try:
            from tree_sitter import Language, Parser
            
            # Load Go language from tree-sitter-go package
            try:
                # tree-sitter-go package structure
                import tree_sitter_go
                # The language() function returns the language object
                self.language = Language(tree_sitter_go.language())
            except (ImportError, AttributeError):
                # Alternative: try to build from source if package not available
                try:
                    import os
                    import tempfile
                    import shutil
                    
                    # Try to find tree-sitter-go in common locations
                    possible_paths = [
                        os.path.join(os.path.dirname(__file__), '..', 'vendor', 'tree-sitter-go'),
                        os.path.expanduser('~/.local/share/tree-sitter-go'),
                    ]
                    
                    go_lang_path = None
                    for path in possible_paths:
                        if os.path.exists(path):
                            go_lang_path = path
                            break
                    
                    if go_lang_path:
                        # Build language library in a temporary location
                        import tempfile
                        tmpdir = tempfile.gettempdir()
                        lib_path = os.path.join(tmpdir, 'tree_sitter_go.so')
                        
                        # Only build if not already built
                        if not os.path.exists(lib_path):
                            Language.build_library(lib_path, [go_lang_path])
                        
                        self.language = Language(lib_path)
                    else:
                        raise ImportError("tree-sitter-go not found")
                except Exception as e:
                    print(f"Warning: Could not load tree-sitter-go: {e}")
                    print("Falling back to regex parsing. Install tree-sitter-go for better accuracy.")
                    print("Install with: pip install tree-sitter tree-sitter-go")
                    self.language = None
                    return
            
            self.parser = Parser(self.language)
        except ImportError as e:
            print(f"Warning: tree-sitter not available: {e}")
            print("Install with: pip install tree-sitter tree-sitter-go")
            self.language = None
            self.parser = None
    
    def parse_file(self, file_path: Path) -> Optional[tree_sitter.Tree]:
        """Parse a Go file and return the syntax tree."""
        if not self.parser:
            return None
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = self.parser.parse(bytes(content, 'utf8'))
            return tree
        except Exception as e:
            print(f"Warning: Could not parse {file_path}: {e}")
            return None
    
    def get_node_text(self, node: tree_sitter.Node, source: bytes) -> str:
        """Extract text content from a node."""
        return source[node.start_byte:node.end_byte].decode('utf-8')
    
    def find_nodes_by_type(self, tree: tree_sitter.Tree, node_type: str) -> List[tree_sitter.Node]:
        """Find all nodes of a specific type in the tree."""
        if not tree:
            return []
        
        nodes = []
        
        def traverse(node: tree_sitter.Node):
            if node.type == node_type:
                nodes.append(node)
            for child in node.children:
                traverse(child)
        
        traverse(tree.root_node)
        return nodes
    
    def get_comment_before_node(self, node: tree_sitter.Node, source: bytes) -> str:
        """Extract comment group immediately before a node."""
        comments = []
        
        # Get the line number of the node
        node_line = node.start_point[0]
        
        # Parse the source to find comments
        lines = source[:node.start_byte].decode('utf-8').split('\n')
        
        # Look backwards from the node's line for consecutive comment lines
        i = node_line - 1
        while i >= 0 and i < len(lines):
            line = lines[i].strip()
            if line.startswith('//'):
                comments.insert(0, line.lstrip('/').strip())
                i -= 1
            elif line == '':
                # Allow one blank line between comments and node
                if i == node_line - 1:
                    i -= 1
                else:
                    break
            else:
                break
        
        return '\n'.join(comments)
    
    def extract_function_signature(self, func_node: tree_sitter.Node, source: bytes) -> Dict:
        """Extract function signature information from a function node."""
        result = {
            'name': '',
            'receiver': None,
            'params': '',
            'returns': '',
            'comment': ''
        }
        
        # Get comment
        result['comment'] = self.get_comment_before_node(func_node, source)
        
        # For method_declaration: receiver, name, parameters, result
        # For function_declaration: name, parameters, result
        is_method = func_node.type == 'method_declaration'
        
        # Find function name and parameters
        name_found = False
        for child in func_node.children:
            if child.type == 'field_identifier' or child.type == 'identifier':
                if not name_found:
                    result['name'] = self.get_node_text(child, source)
                    name_found = True
            elif child.type == 'parameter_list':
                if is_method and not result['receiver']:
                    # First parameter list in method is receiver
                    result['receiver'] = self.get_node_text(child, source)
                else:
                    result['params'] = self.get_node_text(child, source)
            elif child.type == 'parameter_declaration_list':
                result['params'] = self.get_node_text(child, source)
            elif child.type == 'type_identifier':
                # Might be return type, but usually in result node
                pass
        
        # Look for result (return type)
        # Result can be: type_identifier, parameter_list (for multiple returns), etc.
        # We'll extract the full result node if present
        for child in func_node.children:
            if child.type in ['type_identifier', 'pointer_type', 'slice_type']:
                if not result['returns']:
                    result['returns'] = self.get_node_text(child, source)
        
        return result
    
    def extract_struct_fields(self, struct_node: tree_sitter.Node, source: bytes) -> List[Dict]:
        """Extract field definitions from a struct type."""
        fields = []
        
        field_declaration_list = None
        for child in struct_node.children:
            if child.type == 'field_declaration_list':
                field_declaration_list = child
                break
        
        if not field_declaration_list:
            return fields
        
        for child in field_declaration_list.children:
            if child.type == 'field_declaration':
                field = self._parse_field_declaration(child, source)
                if field:
                    fields.append(field)
        
        return fields
    
    def _parse_field_declaration(self, field_node: tree_sitter.Node, source: bytes) -> Optional[Dict]:
        """Parse a single field declaration."""
        field = {
            'name': '',
            'type': '',
            'json_tag': None
        }
        
        # Find field names (can be multiple for same type)
        names = []
        field_type = None
        tags = None
        
        for child in field_node.children:
            if child.type == 'field_identifier':
                names.append(self.get_node_text(child, source))
            elif child.type in ['type_identifier', 'pointer_type', 'slice_type', 'map_type', 'array_type']:
                field_type = self.get_node_text(child, source)
            elif child.type == 'raw_string_literal' or child.type == 'interpreted_string_literal':
                tags = self.get_node_text(child, source).strip('`"')
        
        if not names:
            return None
        
        # Use first name
        field['name'] = names[0]
        field['type'] = field_type or 'unknown'
        
        # Extract JSON tag from protobuf or standard tags
        if tags:
            import re
            # Try JSON tag first
            json_match = re.search(r'json:"([^"]+)"', tags)
            if json_match:
                json_tag = json_match.group(1)
                # Handle omitempty and other options
                json_tag = json_tag.split(',')[0]  # Get first part before comma
                if json_tag != '-':  # Skip omit fields
                    field['json_tag'] = json_tag
            else:
                # Try protobuf tag which might have json info
                protobuf_match = re.search(r'protobuf:"[^"]*json=([^,]+)', tags)
                if protobuf_match:
                    field['json_tag'] = protobuf_match.group(1)
        
        # Default: use field name in camelCase/snake_case
        if not field['json_tag'] or field['json_tag'] == '-':
            # Convert field name to JSON-friendly format
            field_name = field['name']
            # Handle snake_case
            if '_' in field_name:
                parts = field_name.split('_')
                field['json_tag'] = parts[0] + ''.join(p.capitalize() for p in parts[1:])
            else:
                field['json_tag'] = field_name
        
        return field
    
    def is_available(self) -> bool:
        """Check if tree-sitter is available."""
        return self.parser is not None and self.language is not None
