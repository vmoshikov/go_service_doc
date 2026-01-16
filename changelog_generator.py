#!/usr/bin/env python3
"""
CHANGELOG Generator

Automatically generates and updates CHANGELOG.md based on git commits and code changes
using tree-sitter analysis and AI, following keepachangelog.com format.
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from generators.ai_changelog import generate_changelog_entry
from changelog.git_analyzer import GitAnalyzer
from changelog.code_analyzer import CodeAnalyzer


class ChangelogGenerator:
    def __init__(self, go_dir: Path):
        self.go_dir = go_dir
        self.changelog_path = go_dir / 'CHANGELOG.md'
        self.git_analyzer = GitAnalyzer(go_dir)
        self.code_analyzer = CodeAnalyzer(go_dir)
    
    def generate(self, version: Optional[str] = None, since: Optional[str] = None):
        """Generate or update CHANGELOG.md"""
        
        # Get git changes
        print("Analyzing git history...")
        commits = self.git_analyzer.get_commits_since(since)
        
        if not commits:
            print("No new commits found.")
            return
        
        print(f"Found {len(commits)} commit(s)")
        
        # Analyze code changes
        print("Analyzing code changes...")
        changes = self.code_analyzer.analyze_changes(commits)
        
        # Generate changelog entries
        print("Generating changelog entries...")
        changelog_entries = self._generate_entries(changes, version)
        
        # Update CHANGELOG.md
        print("Updating CHANGELOG.md...")
        self._update_changelog(changelog_entries, version)
        
        print(f"CHANGELOG.md updated successfully!")
    
    def _generate_entries(self, changes: Dict, version: Optional[str]) -> List[Dict]:
        """Generate changelog entries using AI"""
        entries = []
        
        for change_type, items in changes.items():
            if not items:
                continue
            
            # Generate AI description for each change
            for item in items:
                entry = generate_changelog_entry(
                    change_type=change_type,
                    item=item
                )
                entries.append({
                    'type': change_type,
                    'description': entry,
                    'item': item
                })
        
        return entries
    
    def _update_changelog(self, entries: List[Dict], version: Optional[str]):
        """Update CHANGELOG.md following keepachangelog.com format"""
        
        # Group entries by type
        added = [e for e in entries if e['type'] == 'added']
        changed = [e for e in entries if e['type'] == 'changed']
        deprecated = [e for e in entries if e['type'] == 'deprecated']
        removed = [e for e in entries if e['type'] == 'removed']
        fixed = [e for e in entries if e['type'] == 'fixed']
        security = [e for e in entries if e['type'] == 'security']
        
        # Determine version
        if not version:
            version = self._get_next_version()
        
        # Read existing changelog
        existing_content = ""
        if self.changelog_path.exists():
            existing_content = self.changelog_path.read_text(encoding='utf-8')
        
        # Generate new section
        new_section = self._generate_section(
            version=version,
            date=datetime.now().strftime('%Y-%m-%d'),
            added=added,
            changed=changed,
            deprecated=deprecated,
            removed=removed,
            fixed=fixed,
            security=security
        )
        
        # Insert new section after header
        if existing_content.startswith('# Changelog'):
            # Insert after header
            lines = existing_content.split('\n')
            insert_pos = 1
            for i, line in enumerate(lines[1:], 1):
                if line.startswith('## ['):
                    insert_pos = i
                    break
            
            lines.insert(insert_pos, '')
            lines.insert(insert_pos + 1, new_section)
            new_content = '\n'.join(lines)
        else:
            # Create new changelog
            header = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),\nand this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n"
            new_content = header + new_section
        
        # Write updated changelog
        self.changelog_path.write_text(new_content, encoding='utf-8')
    
    def _generate_section(self, version: str, date: str, added: List, changed: List,
                         deprecated: List, removed: List, fixed: List, security: List) -> str:
        """Generate a changelog section"""
        lines = [f"## [{version}] - {date}", ""]
        
        if added:
            lines.append("### Added")
            for entry in added:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        if changed:
            lines.append("### Changed")
            for entry in changed:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        if deprecated:
            lines.append("### Deprecated")
            for entry in deprecated:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        if removed:
            lines.append("### Removed")
            for entry in removed:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        if fixed:
            lines.append("### Fixed")
            for entry in fixed:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        if security:
            lines.append("### Security")
            for entry in security:
                lines.append(f"- {entry['description']}")
            lines.append("")
        
        return '\n'.join(lines)
    
    def _get_next_version(self) -> str:
        """Get next version from git tags or default to 0.1.0"""
        try:
            result = subprocess.run(
                ['git', 'describe', '--tags', '--abbrev=0'],
                cwd=self.go_dir,
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                current_version = result.stdout.strip().lstrip('v')
                # Simple increment - in production, use proper semver parsing
                parts = current_version.split('.')
                if len(parts) == 3:
                    patch = int(parts[2]) + 1
                    return f"{parts[0]}.{parts[1]}.{patch}"
            
            return "0.1.0"
        except Exception:
            return "0.1.0"


def main():
    parser = argparse.ArgumentParser(
        description='Generate CHANGELOG.md from git history and code changes'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Path to the Go service directory'
    )
    parser.add_argument(
        '--version',
        type=str,
        help='Version number (e.g., 1.0.0). If not provided, auto-increments from git tags'
    )
    parser.add_argument(
        '--since',
        type=str,
        help='Analyze commits since this tag/commit (e.g., v1.0.0 or HEAD~10)'
    )
    
    args = parser.parse_args()
    
    go_dir = Path(args.directory)
    if not go_dir.exists():
        print(f"Error: Directory '{go_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    generator = ChangelogGenerator(go_dir)
    generator.generate(version=args.version, since=args.since)


if __name__ == '__main__':
    main()
