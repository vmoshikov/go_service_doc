"""
AI Changelog Generator

Generates changelog entries using AI based on code changes.
"""

from typing import Dict


def generate_changelog_entry(change_type: str, item: Dict) -> str:
    """
    Generate a changelog entry description using AI.
    
    Args:
        change_type: Type of change (added, changed, removed, fixed, security, deprecated)
        item: Change item dictionary with details
    
    Returns:
        Generated changelog entry text
    """
    # TODO: Replace with actual AI API call
    # For now, return a demo description based on change information
    
    change_action = item.get('action', '')
    item_type = item.get('type', '')
    name = item.get('name', '')
    file_path = item.get('file', '')
    message = item.get('message', '')
    
    # Build description based on type
    if item_type == 'function':
        if change_action == 'added':
            description = f"Added `{name}()` function"
            if file_path:
                # Extract directory/package name
                parts = file_path.split('/')
                if len(parts) > 1:
                    pkg = parts[-2] if parts[-2] != '.' else parts[-1].replace('.go', '')
                    description += f" in {pkg} package"
        elif change_action == 'removed':
            description = f"Removed `{name}()` function"
            if file_path:
                parts = file_path.split('/')
                if len(parts) > 1:
                    pkg = parts[-2] if parts[-2] != '.' else parts[-1].replace('.go', '')
                    description += f" from {pkg} package"
        elif change_action == 'changed':
            description = f"Updated `{name}()` function"
            if file_path:
                parts = file_path.split('/')
                if len(parts) > 1:
                    pkg = parts[-2] if parts[-2] != '.' else parts[-1].replace('.go', '')
                    description += f" in {pkg} package"
        else:
            description = f"Modified `{name}()` function"
    
    elif item_type == 'api':
        api_type = item.get('api_type', '')
        if api_type == 'rest':
            method = item.get('method', '')
            path = item.get('path', '')
            if change_action == 'added':
                description = f"Added {method} {path} endpoint"
            elif change_action == 'removed':
                description = f"Removed {method} {path} endpoint"
            else:
                description = f"Updated {method} {path} endpoint"
        else:
            description = f"Modified API endpoint"
    else:
        # Generic description
        if change_action == 'added':
            description = f"Added {name or 'new feature'}"
        elif change_action == 'removed':
            description = f"Removed {name or 'feature'}"
        else:
            description = f"Updated {name or 'feature'}"
    
    # Add context from commit message if available
    if message and len(message) < 100:
        # Use commit message as additional context
        description += f" ({message})"
    
    return description
