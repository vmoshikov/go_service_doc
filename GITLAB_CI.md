# GitLab CI Integration Guide

This guide explains how to set up the documentation generator to run as a GitLab CI job in a docs repository.

## Overview

The service is designed to run as a GitLab CI job that:
- Triggers from external repositories via webhooks
- Generates documentation for each project
- Stores documentation in project-specific directories
- Supports corporate VPN pip configuration

## Repository Structure

```
docs-repo/
├── .gitlab-ci.yml          # CI configuration
├── docs/                   # Generated documentation root
│   ├── project1/          # Documentation for project1
│   │   ├── README.md
│   │   └── docs/
│   ├── project2/          # Documentation for project2
│   │   ├── README.md
│   │   └── docs/
│   └── project_id/        # Each project has its own directory
│       └── user/          # User-provided documentation
│           ├── user_architecture.md
│           └── user_db_structure.md
└── doc_generator.py       # Documentation generator
```

## GitLab CI Configuration

### Basic Setup

The `.gitlab-ci.yml` is already configured. You need to set up:

1. **CI/CD Variables** in GitLab Settings:
   - `CI_PIP_INDEX_URL` - Corporate PyPI URL (e.g., `https://pypi.company.com/simple`)
   - `CI_PIP_TRUSTED_HOST` - Corporate PyPI hostname (e.g., `pypi.company.com`)

2. **Project Variables** (optional):
   - `PROJECT_REPO_URL` - External repository URL to clone
   - `PROJECT_REF` - Branch/tag to checkout (default: main)
   - `PROJECT_PATH` - Local path to project (if not cloning)

### Manual Trigger

Trigger the job manually:

```bash
# Via GitLab UI: CI/CD > Pipelines > Run Pipeline
# Or via API:
curl -X POST \
  -F token=YOUR_TRIGGER_TOKEN \
  -F ref=main \
  -F "variables[PROJECT_REPO_URL]=https://gitlab.com/group/project.git" \
  -F "variables[PROJECT_REF]=main" \
  https://gitlab.com/api/v4/projects/PROJECT_ID/trigger/pipeline
```

### Webhook Trigger

Set up webhook in external repository to trigger docs generation:

1. Go to external project: Settings > Webhooks
2. Add webhook URL: `https://gitlab.com/api/v4/projects/DOCS_PROJECT_ID/trigger/pipeline`
3. Set trigger token
4. Select events: Push events, Tag push events

## Corporate VPN Configuration

### Option 1: CI/CD Variables (Recommended)

Set in GitLab: Settings > CI/CD > Variables

```
CI_PIP_INDEX_URL = https://your-corporate-pypi.com/simple
CI_PIP_TRUSTED_HOST = your-corporate-pypi.com
```

### Option 2: pip.conf in Repository

Create `pip.conf` in repository root:

```ini
[global]
index-url = https://your-corporate-pypi.com/simple
trusted-host = your-corporate-pypi.com
```

The CI job will automatically use it.

## User Documentation Structure

User-provided documentation should be stored in:

```
docs/
└── <project_id>/
    └── user/
        ├── user_architecture.md
        ├── user_db_structure.md
        └── other_custom.md
```

Where `<project_id>` is derived from project path (e.g., `group_project` from `group/project`).

## Project Identification

Projects are identified by their path:
- `group/project` → `group_project`
- `namespace:project` → `namespace_project`

This creates unique directories for each project's documentation.

## Example Workflow

1. **External repository** pushes changes
2. **Webhook** triggers GitLab CI job in docs repository
3. **CI job**:
   - Clones external repository
   - Generates documentation
   - Copies user docs from `docs/<project_id>/user/`
   - Saves everything to `docs/<project_id>/`
4. **Documentation** is committed and available in docs repository

## Environment Variables

### Required
- `PROJECT_REPO_URL` or `PROJECT_PATH` - Source of Go service

### Optional
- `PROJECT_REF` - Branch/tag to checkout (default: main)
- `CI_PIP_INDEX_URL` - Corporate PyPI URL
- `CI_PIP_TRUSTED_HOST` - Corporate PyPI hostname
- `DOCS_ROOT` - Documentation root directory (default: docs)

## Troubleshooting

### pip Installation Fails

1. Check `CI_PIP_INDEX_URL` and `CI_PIP_TRUSTED_HOST` variables
2. Verify VPN access from GitLab runners
3. Check pip.conf if using file-based configuration

### Documentation Not Generated

1. Verify project path is correct
2. Check GitLab CI job logs
3. Ensure Go service repository is accessible
4. Verify user docs directory structure

### User Docs Not Found

1. Check directory structure: `docs/<project_id>/user/`
2. Verify project_id matches (use underscores, not slashes)
3. Ensure files have correct names (`user_architecture.md`, etc.)
