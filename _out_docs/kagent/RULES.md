# RULES

Этот файл сгенерирован автоматически и отражает применённые правила генерации.

```json
{
  "language": "ru",
  "features": {
    "thin_readme": true,
    "emoji": true,
    "import_clone": {
      "enabled": false,
      "max_repos": 8,
      "hosts": [],
      "overrides": {}
    }
  },
  "conflicts": {
    "imports_vs_libraries": "prefer_imports"
  },
  "sections": {
    "architecture_user": {
      "enabled": true,
      "source": "user"
    },
    "db_user": {
      "enabled": false,
      "source": "user"
    },
    "diagrams": {
      "enabled": true,
      "source": "auto"
    },
    "imports": {
      "enabled": true,
      "source": "auto"
    },
    "structures": {
      "enabled": true,
      "source": "auto"
    },
    "functions": {
      "enabled": true,
      "source": "auto"
    },
    "api": {
      "enabled": true,
      "source": "auto"
    },
    "tests": {
      "enabled": true,
      "source": "auto"
    },
    "libraries": {
      "enabled": false,
      "source": "auto"
    },
    "others_user": {
      "enabled": true,
      "source": "user"
    }
  },
  "readme_order": [
    "architecture_user",
    "db_user",
    "diagrams",
    "imports",
    "structures",
    "functions",
    "api",
    "tests",
    "libraries",
    "others_user"
  ],
  "repo": {
    "name": "kagent",
    "ref": "main",
    "web_url": "https://example.com/repo"
  }
}
```
