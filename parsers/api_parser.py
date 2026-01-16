"""
API Parser for Go code

Extracts gRPC and REST API endpoints, their handlers, comments, and parameter structures.
Uses tree-sitter for accurate struct parsing, falls back to regex if unavailable.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from parsers.tree_sitter_helper import TreeSitterGoParser
from config import Config


class APIParser:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.structs = {}
        self.ts_parser = TreeSitterGoParser()
        self.use_tree_sitter = self.ts_parser.is_available()
        self.config = Config(go_dir)
    
    def parse(self) -> Dict:
        """Parse all API endpoints from the codebase."""
        # First, collect all struct definitions for parameter extraction
        self._parse_structs()
        
        # Find API-related files
        api_endpoints = []
        
        # Look for gRPC service definitions
        grpc_endpoints = self._parse_grpc()
        
        # Look for REST/HTTP handlers
        rest_endpoints = self._parse_rest()
        
        return {
            'grpc': grpc_endpoints,
            'rest': rest_endpoints,
            'structs': self.structs
        }
    
    def _parse_structs(self):
        """Parse all struct definitions to understand request/response types."""
        go_files = list(self.go_dir.rglob('*.go'))
        go_files = [
            f for f in go_files
            if not f.name.endswith('_test.go') and 'vendor' not in str(f)
        ]
        
        for go_file in go_files:
            if self.use_tree_sitter:
                self._parse_structs_tree_sitter(go_file)
            else:
                self._parse_structs_regex(go_file)
    
    def _parse_structs_tree_sitter(self, go_file: Path):
        """Parse structs using tree-sitter."""
        try:
            content = go_file.read_text(encoding='utf-8')
            source_bytes = bytes(content, 'utf-8')
        except Exception:
            return
        
        tree = self.ts_parser.parse_file(go_file)
        if not tree:
            # Fallback to regex
            self._parse_structs_regex(go_file)
            return
        
        # Find all type declarations
        type_decls = self.ts_parser.find_nodes_by_type(tree, 'type_declaration')
        
        for type_decl in type_decls:
            # Find type spec
            type_spec = None
            struct_name = None
            
            for child in type_decl.children:
                if child.type == 'type_spec':
                    type_spec = child
                    # Get type name
                    for grandchild in child.children:
                        if grandchild.type == 'type_identifier':
                            struct_name = self.ts_parser.get_node_text(grandchild, source_bytes)
                            break
                    break
            
            if not type_spec or not struct_name:
                continue
            
            # Check if it's a struct type
            struct_type = None
            for child in type_spec.children:
                if child.type == 'struct_type':
                    struct_type = child
                    break
            
            if struct_type:
                # Extract fields
                fields = self.ts_parser.extract_struct_fields(struct_type, source_bytes)
                
                if fields:
                    self.structs[struct_name] = {
                        'fields': fields,
                        'file': str(go_file.relative_to(self.go_dir))
                    }
    
    def _parse_structs_regex(self, go_file: Path):
        """Parse structs using regex (fallback)."""
        try:
            content = go_file.read_text(encoding='utf-8')
        except Exception:
            return
        
        struct_pattern = re.compile(
            r'type\s+(\w+)\s+struct\s*\{([^}]+)\}',
            re.MULTILINE | re.DOTALL
        )
        
        matches = struct_pattern.finditer(content)
        for match in matches:
            struct_name = match.group(1)
            struct_body = match.group(2)
            
            # Parse struct fields
            fields = self._parse_struct_fields(struct_body)
            if fields:
                self.structs[struct_name] = {
                    'fields': fields,
                    'file': str(go_file.relative_to(self.go_dir))
                }
    
    def _parse_struct_fields(self, struct_body: str) -> List[Dict]:
        """Parse fields from a struct body."""
        fields = []
        
        # Pattern: FieldName Type `json:"tag"` or FieldName Type
        field_pattern = re.compile(
            r'(\w+)\s+([^\s`]+)(?:\s+`([^`]+)`)?',
            re.MULTILINE
        )
        
        for line in struct_body.split('\n'):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            match = field_pattern.match(line)
            if match:
                field_name = match.group(1)
                field_type = match.group(2).strip()
                tags = match.group(3) if match.group(3) else ''
                
                # Extract JSON tag from protobuf or standard tags
                json_tag = None
                if tags:
                    # Try JSON tag first
                    json_match = re.search(r'json:"([^"]+)"', tags)
                    if json_match:
                        json_tag = json_match.group(1).split(',')[0]  # Get first part before comma
                        if json_tag == '-':  # Skip omit fields
                            json_tag = None
                    else:
                        # Try protobuf tag which might have json info
                        protobuf_match = re.search(r'protobuf:"[^"]*json=([^,]+)', tags)
                        if protobuf_match:
                            json_tag = protobuf_match.group(1)
                
                # Default: convert field name to JSON-friendly format
                if not json_tag or json_tag == '-':
                    # Handle snake_case
                    if '_' in field_name:
                        parts = field_name.split('_')
                        json_tag = parts[0] + ''.join(p.capitalize() for p in parts[1:])
                    else:
                        json_tag = field_name
                
                fields.append({
                    'name': field_name,
                    'type': field_type,
                    'json_tag': json_tag
                })
        
        return fields
    
    def _parse_grpc(self) -> List[Dict]:
        """Parse gRPC service definitions."""
        endpoints = []
        
        go_files = list(self.go_dir.rglob('*.go'))
        go_files = [
            f for f in go_files
            if not f.name.endswith('_test.go') and 'vendor' not in str(f)
        ]
        
        # Pattern for gRPC service methods
        # Look for methods that implement gRPC service interface
        grpc_pattern = re.compile(
            r'(?:^|\n)(?P<comment>(?:^\s*//.*\n)*)'  # Comments
            r'\s*func\s+'
            r'\([^)]+\)\s*'  # Receiver
            r'(?P<method>\w+)'  # Method name
            r'\s*\([^)]*ctx[^)]*,\s*(?P<request>\w+)\s*\*?(?P<request_type>[\w.]+)\)'  # Request
            r'\s*\([^)]*\)\s*\*?(?P<response_type>[\w.]+)'  # Response
            r'\s*error',
            re.MULTILINE
        )
        
        # Also look for proto-generated code patterns
        proto_pattern = re.compile(
            r'(?:^|\n)(?P<comment>(?:^\s*//.*\n)*)'
            r'\s*func\s+\([^)]+\)\s*'
            r'(?P<method>\w+)'
            r'\s*\([^)]*context\.Context[^)]*,\s*\*?(?P<request_type>[\w.]+)\)'
            r'\s*\([^)]*\*?(?P<response_type>[\w.]+)[^)]*,\s*error\)',
            re.MULTILINE
        )
        
        for go_file in go_files:
            try:
                content = go_file.read_text(encoding='utf-8')
            except Exception:
                continue
            
            # Try both patterns
            for pattern in [grpc_pattern, proto_pattern]:
                matches = pattern.finditer(content)
                for match in matches:
                    comment = match.group('comment') or ''
                    method = match.group('method')
                    request_type = match.group('request_type')
                    response_type = match.group('response_type')
                    
                    # Clean comment
                    comment_lines = [
                        line.strip().lstrip('//').strip()
                        for line in comment.split('\n')
                        if line.strip().startswith('//')
                    ]
                    comment_text = '\n'.join(comment_lines)
                    
                    # Get request/response structures
                    request_struct = self._get_struct_json(request_type)
                    response_struct = self._get_struct_json(response_type)
                    
                    # Check for external proto repository
                    proto_link = None
                    proto_repo = None
                    if '.' in request_type or '.' in response_type:
                        # Try to extract package name
                        package_parts = request_type.split('.') if '.' in request_type else response_type.split('.')
                        if package_parts:
                            package_name = package_parts[0]
                            repo_info = self.config.get_proto_repo(package_name)
                            if repo_info:
                                proto_repo = repo_info.get('description', repo_info.get('url', ''))
                                proto_link = self.config.get_proto_link(package_name)
                    
                    endpoints.append({
                        'type': 'grpc',
                        'method': method,
                        'request_type': request_type,
                        'response_type': response_type,
                        'request_json': request_struct,
                        'response_json': response_struct,
                        'comment': comment_text,
                        'file': str(go_file.relative_to(self.go_dir)),
                        'proto_repo': proto_repo,
                        'proto_link': proto_link
                    })
        
        return endpoints
    
    def _parse_rest(self) -> List[Dict]:
        """Parse REST/HTTP API endpoints."""
        endpoints = []
        
        go_files = list(self.go_dir.rglob('*.go'))
        go_files = [
            f for f in go_files
            if not f.name.endswith('_test.go') and 'vendor' not in str(f)
        ]
        
        # Common HTTP router patterns
        router_patterns = [
            # Gin: router.GET/POST/PUT/DELETE("/path", handler)
            (r'router\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*"([^"]+)"\s*,\s*(\w+)', 'gin'),
            # Echo: e.GET/POST/PUT/DELETE("/path", handler)
            (r'e\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*"([^"]+)"\s*,\s*(\w+)', 'echo'),
            # Standard net/http: http.HandleFunc("/path", handler)
            (r'http\.(HandleFunc|Handle)\s*\(\s*"([^"]+)"\s*,\s*(\w+)', 'net/http'),
            # Mux: mux.HandleFunc("/path", handler)
            (r'mux\.HandleFunc\s*\(\s*"([^"]+)"\s*,\s*(\w+)', 'mux'),
        ]
        
        for go_file in go_files:
            try:
                content = go_file.read_text(encoding='utf-8')
            except Exception:
                continue
            
            for pattern, router_type in router_patterns:
                matches = re.finditer(pattern, content)
                for match in matches:
                    if router_type == 'mux':
                        method = 'GET'  # Default, need to check handler
                        path = match.group(1)
                        handler = match.group(2)
                    else:
                        method = match.group(1)
                        path = match.group(2)
                        handler = match.group(3)
                    
                    # Find handler function definition
                    handler_info = self._find_handler_function(content, handler)
                    
                    endpoints.append({
                        'type': 'rest',
                        'method': method,
                        'path': path,
                        'handler': handler,
                        'router': router_type,
                        'comment': handler_info.get('comment', ''),
                        'params': handler_info.get('params', {}),
                        'file': str(go_file.relative_to(self.go_dir))
                    })
        
        return endpoints
    
    def _find_handler_function(self, content: str, handler_name: str) -> Dict:
        """Find handler function and extract its parameters."""
        # Pattern to find function definition
        func_pattern = re.compile(
            r'(?:^|\n)(?P<comment>(?:^\s*//.*\n)*)'
            r'\s*func\s+'
            r'(?:\([^)]+\)\s+)?'
            f'{re.escape(handler_name)}'
            r'\s*\((?P<params>[^)]+)\)',
            re.MULTILINE
        )
        
        match = func_pattern.search(content)
        if match:
            comment = match.group('comment') or ''
            params = match.group('params')
            
            comment_lines = [
                line.strip().lstrip('//').strip()
                for line in comment.split('\n')
                if line.strip().startswith('//')
            ]
            comment_text = '\n'.join(comment_lines)
            
            # Parse parameters (typically *gin.Context, echo.Context, http.ResponseWriter, etc.)
            param_info = {}
            if params:
                # Extract request/response types
                if 'gin.Context' in params:
                    param_info['framework'] = 'gin'
                elif 'echo.Context' in params:
                    param_info['framework'] = 'echo'
                elif 'http.ResponseWriter' in params:
                    param_info['framework'] = 'net/http'
            
            return {
                'comment': comment_text,
                'params': param_info
            }
        
        return {}
    
    def _get_struct_json(self, struct_name: str) -> Optional[Dict]:
        """Get JSON representation of a struct."""
        # Try exact match first
        if struct_name in self.structs:
            return self._struct_to_json(self.structs[struct_name])
        
        # Try without package prefix
        clean_name = struct_name.split('.')[-1]
        if clean_name in self.structs:
            return self._struct_to_json(self.structs[clean_name])
        
        # Try searching by partial name (for cases like pbExample.ListUsersRequest)
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
                # Skip fields with no JSON tag, omit tag, or protobuf internal fields
                continue
            
            # Convert Go types to JSON-compatible types
            json_type = self._go_type_to_json_type(field.get('type', ''))
            json_obj[json_key] = json_type
        
        return json_obj
    
    def _go_type_to_json_type(self, go_type: str):
        """Convert Go type to JSON representation."""
        go_type = go_type.strip()
        
        # Basic types
        type_mapping = {
            'string': 'string',
            'int': 0,
            'int8': 0,
            'int16': 0,
            'int32': 0,
            'int64': 0,
            'uint': 0,
            'uint8': 0,
            'uint16': 0,
            'uint32': 0,
            'uint64': 0,
            'float32': 0.0,
            'float64': 0.0,
            'bool': False,
            'byte': 0,
            'rune': 0,
            'time.Time': '2023-01-01T00:00:00Z',
            'time.Duration': '1s',
        }
        
        if go_type in type_mapping:
            return type_mapping[go_type]
        
        # Pointer types
        if go_type.startswith('*'):
            inner_type = go_type[1:].strip()
            if inner_type in type_mapping:
                return type_mapping[inner_type]
            # For pointer to struct, return None (nullable)
            return None
        
        # Array/Slice types
        if go_type.startswith('[]'):
            return []
        
        # Map types
        if go_type.startswith('map['):
            return {}
        
        # time.Duration (can appear as duration.Duration)
        if 'Duration' in go_type:
            return '1s'
        
        # Default: assume it's a struct or unknown type
        return {}
