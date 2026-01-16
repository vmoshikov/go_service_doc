# PlantUML Diagrams Guide

The documentation generator automatically creates PlantUML diagrams showing component dependencies and architecture.

## Features

- ✅ **Component Dependency Diagrams**: Shows relationships between components/packages
- ✅ **Architecture Diagrams**: High-level view organized by layers (API, Service, Data)
- ✅ **Automatic Detection**: Analyzes your codebase to detect components and dependencies
- ✅ **Visual Documentation**: Makes it easy to understand service structure

## Generated Diagrams

### Component Dependencies Diagram

Shows all components and their dependencies:
- Component names and packages
- Dependency arrows (who depends on whom)
- Component metadata (package name, file count)

### Architecture Diagram

High-level architecture organized by layers:
- **API Layer**: Handlers, endpoints, API components
- **Service Layer**: Business logic, services
- **Data Layer**: Repositories, database access
- Dependencies between layers

## How It Works

1. **Component Analysis**: Scans Go files to identify:
   - Package names
   - Directory structure (components)
   - Import statements (dependencies)

2. **Dependency Detection**: Tracks:
   - Which components import from which
   - Internal vs external dependencies
   - Package relationships

3. **Diagram Generation**: Creates PlantUML diagrams:
   - Component dependency graph
   - Layered architecture view

## Viewing Diagrams

### Option 1: PlantUML Online Server

1. Copy the PlantUML code from `docs/component_diagram.puml`
2. Go to http://www.plantuml.com/plantuml/uml/
3. Paste the code
4. View the rendered diagram

### Option 2: VS Code Extension

Install the "PlantUML" extension:
1. Open VS Code
2. Install "PlantUML" by jebbs
3. Open `.puml` file
4. Press `Alt+D` to preview

### Option 3: IntelliJ IDEA / GoLand

1. Install PlantUML plugin
2. Open `.puml` file
3. View diagram automatically

### Option 4: Command Line

```bash
# Install PlantUML
# macOS
brew install plantuml

# Generate PNG
plantuml docs/component_diagram.puml

# Generate SVG
plantuml -tsvg docs/component_diagram.puml
```

### Option 5: GitHub/GitLab

Both GitHub and GitLab render PlantUML diagrams automatically when you:
1. Commit `.puml` files
2. View them in the repository
3. They render as images automatically

## Diagram Files

The generator creates:
- `docs/component_diagram.puml` - Component dependencies
- `docs/architecture_diagram.puml` - Architecture overview

These are also embedded in the README.md with code blocks.

## Customization

### Component Types

The generator automatically categorizes components:
- **API**: Components with "handler", "api", "endpoint" in name
- **Service**: Components with "service", "business" in name
- **Model**: Components with "model", "entity" in name
- **Repository**: Components with "repo", "db" in name
- **Client**: Components with "client" in name

### Customizing Diagrams

You can edit the generated `.puml` files to:
- Add custom styling
- Group components differently
- Add notes and annotations
- Change colors and themes

## Example Output

```plantuml
@startuml Component Dependencies
!theme plain
skinparam componentStyle rectangle

title Component Dependencies

component "handlers" as handlers #API#
note right of handlers
  Package: handlers
  Files: 5
end note

component "services" as services #Service#
note right of services
  Package: services
  Files: 3
end note

' Dependencies
services --> handlers

@enduml
```

## Integration with README

The diagrams are automatically included in the README.md:
- Appear in "Architecture Diagrams" section
- Placed at the top for visibility
- Include instructions for rendering

## Best Practices

1. **Keep Components Focused**: Each component should have a clear purpose
2. **Minimize Dependencies**: Avoid circular dependencies
3. **Use Clear Names**: Component names should be descriptive
4. **Review Regularly**: Update diagrams as architecture evolves

## Troubleshooting

### No Diagrams Generated

- Check that you have Go files in your project
- Ensure components are detected (check console output)
- Verify directory structure

### Missing Dependencies

- Some dependencies may not be detected if they're external packages
- Internal dependencies within the same component aren't shown
- Only inter-component dependencies are displayed

### Diagram Too Complex

- Consider grouping related components
- Use architecture diagram for high-level view
- Edit `.puml` files to simplify if needed
