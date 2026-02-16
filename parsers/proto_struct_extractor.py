"""
Proto Struct Extractor

Clones external proto repositories and extracts struct definitions
from project-specific directories to enrich API and function documentation.
"""

import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Optional

from config import Config
from parsers.struct_parser import StructParser


class ProtoStructExtractor:
    """Extracts struct definitions from external proto repositories."""
    
    def __init__(self, config: Config, cache_dir: Optional[Path] = None):
        self.config = config
        self.cache_dir = cache_dir or Path(tempfile.gettempdir()) / "proto_cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._struct_cache: Dict[str, Dict] = {}
    
    def get_structs_for_project(self, repo_name: Optional[str] = None) -> Dict[str, Dict]:
        """
        Get struct definitions from proto repository for a specific project.
        
        Returns a dict mapping struct names to their definitions.
        """
        project_name = repo_name or self.config.repo_name
        if not project_name:
            return {}
        
        # Check cache first
        cache_key = f"{project_name}"
        if cache_key in self._struct_cache:
            return self._struct_cache[cache_key]
        
        # Get project path in proto repository
        project_path = self.config.get_proto_path_for_project(project_name)
        if not project_path:
            return {}
        
        # Find which proto repository contains this project
        # For now, use the first proto repository
        # In future, we could add a mapping: project -> proto_repo
        proto_repo_info = None
        for repo_name_key, repo_info in self.config.external_repos.items():
            proto_repo_info = repo_info
            break
        
        if not proto_repo_info:
            return {}
        
        # Clone or use cached proto repository
        repo_url = proto_repo_info.get('url', '')
        branch = proto_repo_info.get('branch', 'main')
        base_path = proto_repo_info.get('path', '')
        
        if not repo_url:
            return {}
        
        # Create cache key for this repo
        repo_cache_key = repo_url.replace('https://', '').replace('http://', '').replace('/', '_')
        repo_cache_dir = self.cache_dir / repo_cache_key
        
        try:
            # Clone repository if not cached
            if not repo_cache_dir.exists():
                print(f"Cloning proto repository: {repo_url}")
                subprocess.run(
                    ['git', 'clone', '--depth', '1', '--branch', branch, '--quiet', repo_url, str(repo_cache_dir)],
                    check=True,
                    capture_output=True
                )
            
            # Build full path to project directory
            # project_path in config is relative to base_path
            # Example: base_path="proto", project_path="kagent" -> proto/kagent
            # Example: base_path="proto", project_path="proto/kagent" -> proto/kagent (already includes base)
            if base_path:
                # Check if project_path already starts with base_path
                if project_path.startswith(base_path + "/") or project_path == base_path:
                    # project_path already includes base_path
                    project_dir = repo_cache_dir / project_path
                else:
                    # project_path is relative to base_path
                    project_dir = repo_cache_dir / base_path / project_path
            else:
                project_dir = repo_cache_dir / project_path
            
            # Normalize path (remove redundant parts)
            try:
                project_dir = project_dir.resolve()
            except Exception:
                # Path might not exist yet, try without resolve
                pass
            
            if not project_dir.exists() or not project_dir.is_dir():
                print(f"Warning: Project path not found in proto repo: {project_dir}")
                print(f"  Base path: {base_path}, Project path: {project_path}")
                return {}
            
            # Extract structs from project directory
            print(f"Extracting structs from proto repository: {project_dir}")
            struct_parser = StructParser(project_dir)
            structs = struct_parser.parse()
            
            # Cache results
            self._struct_cache[cache_key] = structs
            
            return structs
            
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to clone proto repository {repo_url}: {e}")
            return {}
        except Exception as e:
            print(f"Warning: Failed to extract structs from proto repository: {e}")
            return {}
    
    def get_struct(self, struct_name: str, repo_name: Optional[str] = None) -> Optional[Dict]:
        """Get a specific struct definition by name."""
        structs = self.get_structs_for_project(repo_name)
        
        # Try exact match
        if struct_name in structs:
            return structs[struct_name]
        
        # Try without package prefix
        clean_name = struct_name.split('.')[-1]
        if clean_name in structs:
            return structs[clean_name]
        
        # Try partial match
        for key in structs.keys():
            if key.endswith(clean_name) or clean_name in key:
                return structs[key]
        
        return None
