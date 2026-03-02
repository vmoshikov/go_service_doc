"""Path filtering for exclude_dirs (e.g. vendor, third_party)."""

from typing import List


def is_path_excluded(rel_path: str, exclude_dirs: List[str]) -> bool:
    """Return True if rel_path is under any of the exclude_dirs."""
    if not exclude_dirs:
        return False
    rel_path = rel_path.replace("\\", "/")
    for ex in exclude_dirs:
        ex = ex.replace("\\", "/").strip("/")
        if not ex:
            continue
        if rel_path == ex or rel_path.startswith(ex + "/"):
            return True
    return False
