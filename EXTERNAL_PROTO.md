# External Proto Repository Configuration

This guide explains how to configure links to external protobuf repositories.

## Overview

When your Go service uses protobuf definitions from other repositories or directories, you can configure the documentation generator to create links to those external proto definitions.

## Configuration File

Create a `.doc_config.json` file in your Go service root directory:

```json
{
  "external_repositories": {
    "proto-repo": {
      "url": "https://github.com/your-org/proto-definitions",
      "path": "proto",
      "branch": "main",
      "description": "Shared protobuf definitions"
    },
    "common-proto": {
      "url": "https://gitlab.com/your-org/common-proto",
      "path": "definitions",
      "branch": "master",
      "description": "Common proto definitions"
    }
  },
  "proto_mappings": {
    "pbExample": "proto-repo",
    "pbCommon": "common-proto",
    "com.example": "proto-repo"
  }
}
```

## Configuration Fields

### external_repositories

Defines external repositories that contain proto definitions:

- **url**: Repository URL (GitHub, GitLab, or any Git hosting)
- **path**: Path within the repository where proto files are located
- **branch**: Branch name (default: "main" or "master")
- **description**: Human-readable description

### proto_mappings

Maps proto package names to repository names:

- Key: Proto package name or prefix (e.g., `pbExample`, `com.example`)
- Value: Repository name from `external_repositories`

## Examples

### Example 1: Single Proto Repository

```json
{
  "external_repositories": {
    "shared-proto": {
      "url": "https://github.com/mycompany/shared-proto",
      "path": "proto",
      "branch": "main",
      "description": "Shared protobuf definitions"
    }
  },
  "proto_mappings": {
    "pb": "shared-proto",
    "api": "shared-proto"
  }
}
```

### Example 2: Multiple Proto Repositories

```json
{
  "external_repositories": {
    "user-proto": {
      "url": "https://github.com/mycompany/user-service",
      "path": "api/proto",
      "branch": "main",
      "description": "User service proto definitions"
    },
    "order-proto": {
      "url": "https://github.com/mycompany/order-service",
      "path": "proto",
      "branch": "main",
      "description": "Order service proto definitions"
    }
  },
  "proto_mappings": {
    "pbUser": "user-proto",
    "pbOrder": "order-proto"
  }
}
```

### Example 3: Local Directory

If proto files are in a local directory (not a git repo):

```json
{
  "external_repositories": {
    "local-proto": {
      "url": "file:///path/to/proto-definitions",
      "path": "",
      "branch": "",
      "description": "Local proto definitions"
    }
  },
  "proto_mappings": {
    "pb": "local-proto"
  }
}
```

## How It Works

1. **Package Detection**: The generator detects proto package names in your Go code (e.g., `pbExample.ListUsersRequest`)

2. **Mapping Lookup**: It looks up the package name in `proto_mappings` to find the repository

3. **Link Generation**: Creates a link to the proto file in the external repository

4. **Documentation**: Adds the link to the API documentation

## Generated Documentation

When configured, the API documentation will include:

```markdown
### ListUsers

ListUsers is a gRPC method that accepts pbExample.ListUsersRequest and returns pbExample.ListUsersResponse.

**Request Type:** `pbExample.ListUsersRequest` - [View Proto Definition](https://github.com/your-org/proto-definitions/blob/main/proto/example.proto)

**Response Type:** `pbExample.ListUsersResponse` - [View Proto Definition](https://github.com/your-org/proto-definitions/blob/main/proto/example.proto)

*Proto definitions from: Shared protobuf definitions*
```

## Creating Configuration File

You can create an example configuration file:

```bash
python -c "from config import Config; Config.create_example_config(Path('.'))"
```

Or manually create `.doc_config.json` in your Go service root.

## Supported Repository Hosts

- **GitHub**: `https://github.com/owner/repo`
- **GitLab**: `https://gitlab.com/owner/repo`
- **Bitbucket**: `https://bitbucket.org/owner/repo`
- **Generic Git**: Any Git hosting URL
- **Local**: `file:///path/to/directory`

## Troubleshooting

### Links Not Appearing

1. Check that `.doc_config.json` exists in your Go service root
2. Verify package names in `proto_mappings` match your Go imports
3. Ensure repository URLs are correct and accessible

### Wrong Links

1. Check the `path` field matches the actual proto file location
2. Verify the `branch` name is correct
3. Ensure package name mapping is correct

### Multiple Packages from Same Repo

You can map multiple package prefixes to the same repository:

```json
{
  "proto_mappings": {
    "pbUser": "shared-proto",
    "pbOrder": "shared-proto",
    "pbCommon": "shared-proto"
  }
}
```
