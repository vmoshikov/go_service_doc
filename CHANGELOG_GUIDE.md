# CHANGELOG Generator Guide

The CHANGELOG generator automatically creates and updates `CHANGELOG.md` following the [keepachangelog.com](https://keepachangelog.com/) format.

## Features

- ✅ **Git Integration**: Analyzes git commit history
- ✅ **Tree-sitter Analysis**: Understands code changes (functions, APIs, structs)
- ✅ **AI-Powered**: Generates human-readable changelog entries
- ✅ **Standard Format**: Follows keepachangelog.com format
- ✅ **Automatic Categorization**: Groups changes into Added/Changed/Deprecated/Removed/Fixed/Security

## Usage

### Basic Usage

```bash
# Generate changelog for commits since last git tag
python changelog_generator.py /path/to/go-service
```

### With Version

```bash
# Specify version number
python changelog_generator.py /path/to/go-service --version 1.2.0
```

### Since Specific Tag/Commit

```bash
# Analyze commits since a specific tag
python changelog_generator.py /path/to/go-service --since v1.0.0

# Analyze last N commits
python changelog_generator.py /path/to/go-service --since HEAD~10
```

## How It Works

### 1. Git Analysis

The generator:
- Analyzes git commit history
- Extracts commit messages, authors, dates
- Identifies changed files
- Gets diffs for code analysis

### 2. Code Analysis (Tree-sitter)

For each changed file, it detects:
- **Added Functions**: New function definitions
- **Removed Functions**: Deleted functions
- **Changed Functions**: Modified functions
- **API Endpoints**: New/removed REST/gRPC endpoints
- **Struct Changes**: Modified data structures

### 3. AI Generation

Uses AI to generate human-readable descriptions:
- Analyzes function names and signatures
- Understands context from commit messages
- Creates clear, concise changelog entries

### 4. Categorization

Automatically categorizes changes:
- **Added**: New features, functions, endpoints
- **Changed**: Modified existing functionality
- **Deprecated**: Features marked for removal
- **Removed**: Deleted features
- **Fixed**: Bug fixes
- **Security**: Security-related changes

## Output Format

The generated CHANGELOG.md follows this structure:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2024-01-15

### Added
- Added `ListUsers()` function in handlers package
- Added GET /api/users endpoint

### Changed
- Updated `CreateUser()` function in handlers package

### Fixed
- Fixed authentication bug in login handler

### Security
- Fixed SQL injection vulnerability in user query
```

## Commit Message Analysis

The generator analyzes commit messages to categorize changes:

- **Security**: Keywords like "security", "vulnerability", "CVE", "exploit"
- **Fixed**: Keywords like "fix", "bug", "error", "issue"
- **Deprecated**: Keywords like "deprecate", "obsolete"

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: Generate CHANGELOG

on:
  push:
    tags:
      - 'v*'

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Generate CHANGELOG
        run: |
          python changelog_generator.py . --version ${{ github.ref_name }}
      
      - name: Commit CHANGELOG
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add CHANGELOG.md
          git commit -m "Update CHANGELOG for ${{ github.ref_name }}" || exit 0
          git push
```

## Customization

### AI Integration

To use actual AI (instead of demo strings), update `generators/ai_changelog.py`:

```python
def generate_changelog_entry(change_type: str, item: Dict) -> str:
    # Replace with your AI API call
    # Example with OpenAI:
    import openai
    
    prompt = f"Generate a changelog entry for: {change_type} - {item}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

### Custom Categorization

Modify `changelog/code_analyzer.py` to customize how changes are categorized based on your project's conventions.

## Best Practices

1. **Use Semantic Versioning**: Tag releases with `v1.0.0` format
2. **Write Clear Commit Messages**: Helps AI generate better descriptions
3. **Run Before Releases**: Generate changelog before creating a new tag
4. **Review Generated Entries**: AI-generated content should be reviewed
5. **Manual Edits**: You can manually edit CHANGELOG.md - new entries are prepended

## Troubleshooting

### No Commits Found

If you see "No new commits found":
- Check if you have git tags: `git tag`
- Try specifying `--since HEAD~50` to analyze recent commits
- Ensure you're in a git repository

### Missing Changes

The generator focuses on:
- Function definitions
- API endpoints
- Significant code changes

Minor changes (comments, formatting) may not appear. You can manually add entries to CHANGELOG.md.

### Version Detection

If version auto-detection fails:
- Ensure you have git tags: `git tag -a v1.0.0 -m "Release 1.0.0"`
- Or specify version manually: `--version 1.0.0`
