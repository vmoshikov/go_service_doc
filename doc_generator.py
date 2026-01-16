#!/usr/bin/env python3
"""
Go Service Documentation Generator

A service that generates comprehensive documentation for Go services by analyzing
the codebase and combining user-provided sections with auto-generated content.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

from parsers.function_parser import FunctionParser
from parsers.api_parser import APIParser
from parsers.test_parser import TestParser
from parsers.library_parser import LibraryParser
from generators.doc_generator import DocumentationGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Generate documentation for Go service from codebase'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Path to the Go service directory'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='README.md',
        help='Output file name (default: README.md)'
    )
    
    args = parser.parse_args()
    
    # Validate directory path
    go_dir = Path(args.directory)
    if not go_dir.exists():
        print(f"Error: Directory '{go_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not go_dir.is_dir():
        print(f"Error: '{go_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)
    
    # Check for docs directory
    docs_dir = go_dir / 'docs'
    if not docs_dir.exists():
        docs_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created docs directory at {docs_dir}")
    
    # Check for external user docs directory (from docs repo)
    # Format: docs/<project_id>/user/
    user_docs_dir = None
    
    # Try to determine project ID from environment or project path
    project_id = os.environ.get('PROJECT_ID', '')
    if not project_id:
        # Try to extract from PROJECT_REPO_URL or CI_PROJECT_PATH
        project_path = os.environ.get('PROJECT_REPO_URL', '') or os.environ.get('CI_PROJECT_PATH', '')
        if project_path:
            # Extract project identifier (group/project -> group_project)
            project_id = project_path.replace('/', '_').replace(':', '_').replace('.git', '')
    
    if project_id:
        # Look for user docs in docs repo structure
        # In GitLab CI, we're in the docs repository
        docs_repo_root = Path(os.environ.get('CI_PROJECT_DIR', '.'))
        potential_user_docs = docs_repo_root / 'docs' / project_id / 'user'
        if potential_user_docs.exists():
            user_docs_dir = potential_user_docs
            print(f"Found user docs directory: {user_docs_dir}")
        else:
            print(f"User docs directory not found: {potential_user_docs} (will use local docs if available)")
    
    print(f"Analyzing Go service at: {go_dir}")
    
    # Check for config file and create example if needed
    config_path = go_dir / '.doc_config.json'
    if not config_path.exists():
        print(f"Tip: Create .doc_config.json to configure external proto repositories")
        print(f"     See EXTERNAL_PROTO.md for details")
    
    # Initialize parsers
    function_parser = FunctionParser(go_dir)
    api_parser = APIParser(go_dir)
    test_parser = TestParser(go_dir)
    library_parser = LibraryParser(go_dir)
    
    # Parse codebase
    print("Parsing API endpoints and structs...")
    api_spec = api_parser.parse()
    
    # Pass structs to function parser for struct type extraction
    print("Parsing functions...")
    function_parser.set_structs(api_spec.get('structs', {}))
    functions = function_parser.parse()
    
    print("Parsing tests...")
    tests = test_parser.parse()
    
    print("Parsing libraries...")
    libraries = library_parser.parse()
    
    # Generate documentation
    print("Generating documentation...")
    doc_generator = DocumentationGenerator(go_dir, docs_dir, user_docs_dir=user_docs_dir)
    doc_generator.set_structs(api_spec.get('structs', {}))
    doc_generator.generate(
        functions=functions,
        api_spec=api_spec,
        tests=tests,
        libraries=libraries,
        output_file=args.output
    )
    
    print(f"Documentation generated successfully: {go_dir / args.output}")


if __name__ == '__main__':
    main()
