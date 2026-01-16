# Go Service Documentation Generator

A Python service that automatically generates comprehensive documentation for Go services by analyzing the codebase and combining user-provided sections with auto-generated content.

## Features

- **Automatic Code Analysis**: Parses Go source files to extract:
  - Function definitions with signatures and comments
  - gRPC and REST API endpoints
  - Test functions and test cases
  - Dependencies from `go.mod`

- **Documentation Sections**:
  - **Architecture** (`user_architecture.md`) - User-provided
  - **DB Structure** (`user_db_structure.md`) - User-provided (optional)
  - **Functions** (`functions.md`) - Auto-generated
  - **API Specification** (`api.md`) - Auto-generated with JSON representations
  - **Testing** (`test.md`) - Auto-generated
  - **Libraries Used** (`libraries.md`) - Auto-generated
  - **Others** - User-provided (optional)

- **API Documentation**: Extracts gRPC and REST endpoints with:
  - Comments above server descriptions
  - Input and output parameters
  - JSON representations of request/response structures

- **PlantUML Diagrams**: Automatically generates architecture diagrams:
  - Component dependency graphs
  - Layered architecture views
  - Visual representation of service structure

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

The service uses **tree-sitter** for accurate AST-based parsing of Go code, which provides better accuracy than regex-based parsing. If tree-sitter is not available, the service will automatically fall back to regex parsing.

### Dependencies

- `tree-sitter>=0.20.0` - Parser library
- `tree-sitter-go>=0.19.0` - Go language grammar for tree-sitter

## Usage

### Local Installation

```bash
python doc_generator.py <path_to_go_service_directory> [--output README.md]
```

### Docker

Build the Docker image:

```bash
docker build -t go-doc-generator .
```

#### Run as a Service (Recommended)

Start the service container (keeps running for exec access):

```bash
docker run -d --name doc-gen -v /path/to/go-service:/workspace go-doc-generator
```

Execute commands in the running container:

```bash
# Generate documentation
docker exec -it doc-gen doc_generator.py /workspace

# With custom output
docker exec -it doc-gen doc_generator.py /workspace --output CUSTOM_README.md

# Access shell to explore
docker exec -it doc-gen bash

# View files in workspace
docker exec -it doc-gen ls -la /workspace
```

Stop and remove the container:

```bash
docker stop doc-gen && docker rm doc-gen
```

#### Run Once (Execute and Exit)

```bash
docker run --rm -v /path/to/go-service:/workspace go-doc-generator /workspace
```

#### Using Docker Compose

```bash
# Start service
docker-compose up -d

# Execute generator
docker-compose exec doc-generator doc_generator.py /workspace

# Access shell
docker-compose exec doc-generator bash

# Stop service
docker-compose down
```

### Example

```bash
# Local
python doc_generator.py /path/to/my-go-service

# Docker
docker run --rm -v /path/to/my-go-service:/workspace go-doc-generator /workspace
```

This will:
1. Analyze the Go service codebase
2. Generate documentation sections in the `docs/` directory
3. Combine all sections into `README.md` in the service root

## User-Provided Documentation

You can add your own custom documentation sections that will be automatically included in the generated README.md.

### Predefined Sections

Place these files in the `docs/` directory for special handling:

- **`user_architecture.md`** - Service architecture overview (appears first)
- **`user_db_structure.md`** - Database schema and structure (appears second, optional)

### Custom Sections

Any other `.md` files in the `docs/` directory will be automatically included in the "Others" section:

- `deployment.md` - Deployment instructions
- `api_examples.md` - API usage examples
- `troubleshooting.md` - Troubleshooting guide
- Any other markdown files you create

### How to Add Sections

1. Create a markdown file in the `docs/` directory
2. Start with a `# Title` heading
3. Run the documentation generator
4. Your section will appear in the README.md

**Example:**

```markdown
# Deployment Guide

## Prerequisites
- Docker
- Kubernetes

## Steps
1. Build image
2. Deploy
```

See [USER_SECTIONS.md](USER_SECTIONS.md) for detailed instructions and examples.

## Generated Documentation

The service automatically generates:

- **functions.md**: All function definitions with signatures and comments
- **api.md**: Complete API specification with endpoints, parameters, and JSON schemas
- **test.md**: Test functions, benchmarks, and examples
- **libraries.md**: Dependencies from `go.mod`

All sections are automatically combined into a single `README.md` file.

## Supported Frameworks

- **gRPC**: Proto-generated service methods
- **REST**: Gin, Echo, net/http, Gorilla Mux

## Structure

```
go_service_doc/
├── doc_generator.py          # Main entry point
├── parsers/                  # Code parsers
│   ├── function_parser.py
│   ├── api_parser.py
│   ├── test_parser.py
│   └── library_parser.py
├── generators/              # Documentation generators
│   └── doc_generator.py
└── requirements.txt
```

## CHANGELOG Generation

The service includes an automatic CHANGELOG generator that follows [keepachangelog.com](https://keepachangelog.com/) format:

```bash
python changelog_generator.py <path_to_go_service> [--version 1.0.0] [--since v0.9.0]
```

### Features

- **Git Integration**: Analyzes git commits and changes
- **Tree-sitter Analysis**: Understands code changes (functions, APIs, etc.)
- **AI-Powered**: Generates changelog entries using AI
- **Keep a Changelog Format**: Follows standard format with Added/Changed/Deprecated/Removed/Fixed/Security sections
- **Automatic Versioning**: Auto-increments version from git tags

### Usage

```bash
# Generate changelog for all commits since last tag
python changelog_generator.py /path/to/go-service

# Generate changelog with specific version
python changelog_generator.py /path/to/go-service --version 1.2.0

# Generate changelog since specific tag/commit
python changelog_generator.py /path/to/go-service --since v1.0.0
```

## Notes

- The service uses **tree-sitter** for accurate AST-based parsing, providing better handling of:
  - Complex function signatures
  - Struct definitions with embedded types
  - Comments and documentation
  - Edge cases in Go syntax
  
- If tree-sitter is not installed, the service automatically falls back to regex-based parsing
- The service skips `vendor/` directories and test files during parsing
- Struct definitions are parsed to generate JSON representations for API documentation
- Comments above functions and endpoints are preserved in the documentation
