"""
Git Analyzer

Analyzes git history to extract commits and changes.
"""

import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class GitAnalyzer:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def get_tags_sorted(self) -> List[str]:
        """
        Return git tags sorted by creator date (newest first).

        Note: for lightweight tags, `creatordate` can be less reliable than for
        annotated tags, but it's a pragmatic default for "latest release tag".
        """
        try:
            result = subprocess.run(
                ["git", "for-each-ref", "--sort=-creatordate", "--format=%(refname:short)", "refs/tags"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True,
            )
            return [t.strip() for t in result.stdout.splitlines() if t.strip()]
        except Exception:
            return []

    def get_latest_tag(self) -> Optional[str]:
        """Get newest tag by creator date, if any."""
        tags = self.get_tags_sorted()
        return tags[0] if tags else None

    def get_previous_tag(self, tag: str) -> Optional[str]:
        """Get the next older tag relative to `tag` (by creator date order)."""
        tags = self.get_tags_sorted()
        if not tags:
            return None
        try:
            idx = tags.index(tag)
        except ValueError:
            return None
        return tags[idx + 1] if idx + 1 < len(tags) else None

    def get_commits_between(self, older_ref: Optional[str], newer_ref: str) -> List[Dict]:
        """
        Get commits in (older_ref..newer_ref]. If older_ref is None, returns commits
        reachable from newer_ref (up to repo root).
        """
        try:
            range_spec = newer_ref if not older_ref else f"{older_ref}..{newer_ref}"
            result = subprocess.run(
                ["git", "log", "--pretty=format:%H|%s|%b|%an|%ae|%ad", "--date=iso", range_spec],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            commits: List[Dict] = []
            for line in result.stdout.strip().split("\n"):
                if not line:
                    continue
                parts = line.split("|", 5)
                if len(parts) >= 6:
                    commits.append(
                        {
                            "hash": parts[0],
                            "subject": parts[1],
                            "body": parts[2],
                            "author": parts[3],
                            "email": parts[4],
                            "date": parts[5],
                        }
                    )
                elif len(parts) >= 2:
                    commits.append(
                        {
                            "hash": parts[0],
                            "subject": parts[1],
                            "body": "",
                            "author": "",
                            "email": "",
                            "date": "",
                        }
                    )
            return commits
        except Exception as e:
            print(f"Warning: Could not get commits between refs: {e}")
            return []

    def get_diff_name_status(self, older_ref: Optional[str], newer_ref: str) -> List[Tuple[str, str]]:
        """
        Return list of (status, path) from `git diff --name-status`.
        If older_ref is None, falls back to `git show --name-status` for `newer_ref`.
        """
        try:
            if older_ref:
                args = ["git", "diff", "--name-status", f"{older_ref}..{newer_ref}"]
            else:
                args = ["git", "show", "--name-status", "--pretty=format:", newer_ref]

            result = subprocess.run(
                args,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True,
            )
            out: List[Tuple[str, str]] = []
            for line in result.stdout.splitlines():
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                status = parts[0].strip() if parts else ""
                if not status:
                    continue
                # rename format: R100\told\tnew
                if status.startswith("R") and len(parts) >= 3:
                    out.append((status, parts[2].strip()))
                elif len(parts) >= 2:
                    out.append((status, parts[1].strip()))
            return out
        except Exception:
            return []
    
    def get_commits_since(self, since: Optional[str] = None) -> List[Dict]:
        """Get commits since a specific tag/commit"""
        try:
            # Get commit range
            if since:
                range_spec = f"{since}..HEAD"
                log_args = ['git', 'log', '--pretty=format:%H|%s|%b|%an|%ae|%ad', '--date=iso', range_spec]
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
                    log_args = ['git', 'log', '--pretty=format:%H|%s|%b|%an|%ae|%ad', '--date=iso', range_spec]
                else:
                    # No tags, get last 50 commits (safe even for small repos)
                    log_args = ['git', 'log', '--max-count=50', '--pretty=format:%H|%s|%b|%an|%ae|%ad', '--date=iso', 'HEAD']
            
            # Get commits
            result = subprocess.run(
                log_args,
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
