# Adding User Sections to Documentation

You can add your own custom documentation sections that will be automatically included in the generated README.md.

## How It Works

The documentation generator looks for markdown files in the `docs/` directory and includes them in the final README.md in a specific order:

1. **Predefined User Sections** (added first)
2. **Auto-generated Sections** (functions, API, tests, libraries)
3. **Other User Files** (any other .md files in docs/)

## Method 1: Predefined User Sections

These sections are recognized by name and appear at the top of the documentation:

### Architecture Section

Create `docs/user_architecture.md`:

```markdown
# Architecture

## Overview

This service follows a microservices architecture...

## Components

- **API Layer**: Handles HTTP/gRPC requests
- **Service Layer**: Business logic
- **Data Layer**: Database access
```

### Database Structure Section

Create `docs/user_db_structure.md`:

```markdown
# DB Structure

## Tables

### users
- id (UUID, Primary Key)
- email (VARCHAR, Unique)
- created_at (TIMESTAMP)

### orders
- id (UUID, Primary Key)
- user_id (UUID, Foreign Key)
- amount (DECIMAL)
```

## Method 2: Custom User Sections

You can add **any other markdown file** to the `docs/` directory, and it will be automatically included in the "Others" section.

### Example: Adding a Deployment Guide

Create `docs/deployment.md`:

```markdown
# Deployment

## Prerequisites

- Docker
- Kubernetes cluster

## Steps

1. Build the image
2. Push to registry
3. Deploy to cluster
```

### Example: Adding API Usage Examples

Create `docs/api_examples.md`:

```markdown
# API Usage Examples

## Creating a User

```bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'
```
```

## File Naming

- **Predefined sections**: Must use exact names (`user_architecture.md`, `user_db_structure.md`)
- **Custom sections**: Can use any name (e.g., `deployment.md`, `api_examples.md`, `troubleshooting.md`)

## Section Order in README.md

The final README.md will have sections in this order:

1. **Architecture** (if `user_architecture.md` exists)
2. **DB Structure** (if `user_db_structure.md` exists)
3. **Functions** (auto-generated)
4. **API Specification** (auto-generated)
5. **Testing** (auto-generated)
6. **Libraries Used** (auto-generated)
7. **Others** (all other .md files from docs/)

## Best Practices

1. **Use clear titles**: Start each file with a `# Title` heading
2. **Organize with subsections**: Use `##` for main sections, `###` for subsections
3. **Keep files focused**: One topic per file
4. **Use markdown formatting**: Code blocks, lists, tables, etc.

## Example Structure

```
your-go-service/
├── docs/
│   ├── user_architecture.md      # Predefined - appears first
│   ├── user_db_structure.md      # Predefined - appears second
│   ├── deployment.md              # Custom - appears in "Others"
│   ├── api_examples.md            # Custom - appears in "Others"
│   └── troubleshooting.md         # Custom - appears in "Others"
├── handlers/
├── services/
└── README.md                      # Generated - includes all sections
```

## Navigation

All user sections are automatically included in the navigation menu at the top of README.md, making it easy to jump to any section.
