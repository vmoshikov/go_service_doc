"""
Configuration for external repositories and proto locations
"""

import json
from pathlib import Path
from typing import Dict, List, Optional


class Config:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.config_path = go_dir / '.doc_config.json'
        self.external_repos = {}
        self.proto_mappings = {}
        self._load_config()
    
    def _load_config(self):
        """Load configuration from .doc_config.json"""
        if self.config_path.exists():
            try:
                config = json.loads(self.config_path.read_text(encoding='utf-8'))
                self.external_repos = config.get('external_repositories', {})
                self.proto_mappings = config.get('proto_mappings', {})
            except Exception as e:
                print(f"Warning: Could not load config: {e}")
    
    def get_proto_repo(self, proto_package: str) -> Optional[Dict]:
        """Get repository information for a proto package"""
        # Direct mapping
        if proto_package in self.proto_mappings:
            repo_name = self.proto_mappings[proto_package]
            return self.external_repos.get(repo_name)
        
        # Try to match by package prefix
        for package_prefix, repo_name in self.proto_mappings.items():
            if proto_package.startswith(package_prefix):
                return self.external_repos.get(repo_name)
        
        return None
    
    def get_proto_link(self, proto_package: str, proto_file: Optional[str] = None) -> Optional[str]:
        """Get link to proto file in external repository"""
        repo_info = self.get_proto_repo(proto_package)
        if not repo_info:
            return None
        
        base_url = repo_info.get('url', '')
        path = repo_info.get('path', '')
        
        if proto_file:
            # Construct link to specific proto file
            if base_url:
                # GitHub/GitLab style
                if 'github.com' in base_url or 'gitlab.com' in base_url:
                    # Convert to blob/tree URL
                    if '/tree/' not in base_url and '/blob/' not in base_url:
                        base_url = base_url.rstrip('/')
                        branch = repo_info.get('branch', 'main')
                        base_url = f"{base_url}/blob/{branch}"
                    
                    if path:
                        full_path = f"{path}/{proto_file}".lstrip('/')
                    else:
                        full_path = proto_file
                    
                    return f"{base_url}/{full_path}"
                else:
                    # Generic URL
                    if path:
                        return f"{base_url}/{path}/{proto_file}"
                    else:
                        return f"{base_url}/{proto_file}"
        
        return base_url
    
    @staticmethod
    def create_example_config(go_dir: Path):
        """Create an example configuration file"""
        example_config = {
            "external_repositories": {
                "proto-repo": {
                    "url": "https://github.com/your-org/proto-definitions",
                    "path": "proto",
                    "branch": "main",
                    "description": "Shared protobuf definitions"
                },
                "common-proto": {
                    "url": "https://gitlab.com/your-org/common-proto",
                    "path": "definitions",
                    "branch": "master",
                    "description": "Common proto definitions"
                }
            },
            "proto_mappings": {
                "pbExample": "proto-repo",
                "pbCommon": "common-proto",
                "com.example": "proto-repo"
            }
        }
        
        config_path = go_dir / '.doc_config.json'
        config_path.write_text(
            json.dumps(example_config, indent=2),
            encoding='utf-8'
        )
        print(f"Created example config at {config_path}")
        print("Edit .doc_config.json to configure your external repositories")
