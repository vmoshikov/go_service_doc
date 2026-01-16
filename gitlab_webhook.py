#!/usr/bin/env python3
"""
GitLab Webhook Handler

Handles webhook requests from external repositories to trigger documentation generation.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional


def handle_webhook(payload: Dict, docs_root: Path) -> Dict:
    """Handle webhook payload and trigger documentation generation."""
    project_path = payload.get('project', {}).get('path_with_namespace', '')
    project_id = project_path.replace('/', '_').replace(':', '_')
    
    # Get project repository URL
    project_url = payload.get('project', {}).get('git_http_url', '')
    project_ref = payload.get('ref', 'main')
    
    # Create project-specific directory
    project_docs_dir = docs_root / project_id
    project_docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Clone repository temporarily
    clone_dir = Path(f"/tmp/{project_id}")
    
    try:
        # Clone repository
        subprocess.run(
            ['git', 'clone', '--depth', '1', '--branch', project_ref, project_url, str(clone_dir)],
            check=True
        )
        
        # Generate documentation
        result = subprocess.run(
            [sys.executable, 'doc_generator.py', str(clone_dir), '--output', 'README.md'],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode != 0:
            return {
                'success': False,
                'error': result.stderr,
                'project_id': project_id
            }
        
        # Copy generated docs
        source_docs = clone_dir / 'docs'
        if source_docs.exists():
            import shutil
            shutil.copytree(source_docs, project_docs_dir, dirs_exist_ok=True)
        
        source_readme = clone_dir / 'README.md'
        if source_readme.exists():
            import shutil
            shutil.copy(source_readme, project_docs_dir / 'README.md')
        
        # Cleanup
        import shutil
        shutil.rmtree(clone_dir, ignore_errors=True)
        
        return {
            'success': True,
            'project_id': project_id,
            'docs_path': str(project_docs_dir)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'project_id': project_id
        }


def main():
    parser = argparse.ArgumentParser(description='Handle GitLab webhook for documentation generation')
    parser.add_argument('--docs-root', type=str, default='docs', help='Root directory for documentation')
    parser.add_argument('--payload', type=str, help='Webhook payload JSON (or read from stdin)')
    
    args = parser.parse_args()
    
    # Read payload
    if args.payload:
        payload = json.loads(args.payload)
    else:
        payload = json.load(sys.stdin)
    
    docs_root = Path(args.docs_root)
    result = handle_webhook(payload, docs_root)
    
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()
