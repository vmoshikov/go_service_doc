"""
Git Analyzer

Analyzes git history to extract commits and changes.
"""

import subprocess
from pathlib import Path
from typing import Dict, List, Optional


class GitAnalyzer:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
    
    def get_commits_since(self, since: Optional[str] = None) -> List[Dict]:
        """Get commits since a specific tag/commit"""
        try:
            # Get commit range
            if since:
                range_spec = f"{since}..HEAD"
            else:
                # Get last tag or default to all commits
                result = subprocess.run(
                    ['git', 'describe', '--tags', '--abbrev=0'],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True,
                    check=False
                )
                if result.returncode == 0:
                    last_tag = result.stdout.strip()
                    range_spec = f"{last_tag}..HEAD"
                else:
                    # No tags, get last 50 commits
                    range_spec = "HEAD~50..HEAD"
            
            # Get commits
            result = subprocess.run(
                ['git', 'log', '--pretty=format:%H|%s|%b|%an|%ae|%ad', '--date=iso', range_spec],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue
                
                parts = line.split('|', 5)
                if len(parts) >= 6:
                    commits.append({
                        'hash': parts[0],
                        'subject': parts[1],
                        'body': parts[2],
                        'author': parts[3],
                        'email': parts[4],
                        'date': parts[5]
                    })
                elif len(parts) >= 2:
                    commits.append({
                        'hash': parts[0],
                        'subject': parts[1],
                        'body': '',
                        'author': '',
                        'email': '',
                        'date': ''
                    })
            
            return commits
        except subprocess.CalledProcessError as e:
            print(f"Warning: Could not get git commits: {e}")
            return []
        except Exception as e:
            print(f"Warning: Error analyzing git: {e}")
            return []
    
    def get_changed_files(self, commit_hash: str) -> List[str]:
        """Get list of changed files in a commit"""
        try:
            result = subprocess.run(
                ['git', 'show', '--name-only', '--pretty=format:', commit_hash],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            files = []
            for line in result.stdout.strip().split('\n'):
                line = line.strip()
                if line and not line.startswith('commit') and not line.startswith('Author'):
                    files.append(line)
            
            return files
        except Exception:
            return []
    
    def get_file_diff(self, commit_hash: str, file_path: str) -> str:
        """Get diff for a specific file in a commit"""
        try:
            result = subprocess.run(
                ['git', 'show', commit_hash, '--', file_path],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except Exception:
            return ""
