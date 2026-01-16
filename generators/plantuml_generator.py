"""
PlantUML Diagram Generator

Generates PlantUML diagrams for component dependencies and architecture.
"""

from typing import Dict, List, Optional


class PlantUMLGenerator:
    def __init__(self):
        pass
    
    def generate_component_diagram(self, components: Dict) -> str:
        """Generate PlantUML component diagram showing dependencies"""
        lines = [
            "@startuml Component Dependencies",
            "!theme plain",
            "skinparam componentStyle rectangle",
            "skinparam linetype ortho",
            "",
            "title Component Dependencies",
            ""
        ]
        
        # Group components by type for better organization
        api_components = []
        service_components = []
        data_components = []
        other_components = []
        
        for comp_name, comp_info in sorted(components.items()):
            name_lower = comp_name.lower()
            if 'handler' in name_lower or 'api' in name_lower or 'endpoint' in name_lower:
                api_components.append((comp_name, comp_info))
            elif 'service' in name_lower or 'business' in name_lower:
                service_components.append((comp_name, comp_info))
            elif 'repo' in name_lower or 'db' in name_lower or 'data' in name_lower or 'model' in name_lower or 'entity' in name_lower:
                data_components.append((comp_name, comp_info))
            else:
                other_components.append((comp_name, comp_info))
        
        # Add components grouped by type with packages for better layout
        if api_components:
            lines.append("package \"API Components\" {")
            for comp_name, comp_info in api_components:
                package = comp_info.get('package', comp_name)
                display_name = comp_name if comp_name != 'root' else 'main'
                comp_id = self._sanitize_id(comp_name)
                lines.append(f'  component "{display_name}" as {comp_id}')
                lines.append(f'  note right of {comp_id}')
                lines.append(f'    Package: {package}')
                lines.append(f'    Files: {len(comp_info.get("files", []))}')
                lines.append('  end note')
            lines.append("}")
            lines.append("")
        
        if service_components:
            lines.append("package \"Service Components\" {")
            for comp_name, comp_info in service_components:
                package = comp_info.get('package', comp_name)
                display_name = comp_name if comp_name != 'root' else 'main'
                comp_id = self._sanitize_id(comp_name)
                lines.append(f'  component "{display_name}" as {comp_id}')
                lines.append(f'  note right of {comp_id}')
                lines.append(f'    Package: {package}')
                lines.append(f'    Files: {len(comp_info.get("files", []))}')
                lines.append('  end note')
            lines.append("}")
            lines.append("")
        
        if data_components:
            lines.append("package \"Data Components\" {")
            for comp_name, comp_info in data_components:
                package = comp_info.get('package', comp_name)
                display_name = comp_name if comp_name != 'root' else 'main'
                comp_id = self._sanitize_id(comp_name)
                lines.append(f'  component "{display_name}" as {comp_id}')
                lines.append(f'  note right of {comp_id}')
                lines.append(f'    Package: {package}')
                lines.append(f'    Files: {len(comp_info.get("files", []))}')
                lines.append('  end note')
            lines.append("}")
            lines.append("")
        
        if other_components:
            lines.append("package \"Other Components\" {")
            for comp_name, comp_info in other_components:
                package = comp_info.get('package', comp_name)
                display_name = comp_name if comp_name != 'root' else 'main'
                comp_id = self._sanitize_id(comp_name)
                lines.append(f'  component "{display_name}" as {comp_id}')
                lines.append(f'  note right of {comp_id}')
                lines.append(f'    Package: {package}')
                lines.append(f'    Files: {len(comp_info.get("files", []))}')
                lines.append('  end note')
            lines.append("}")
            lines.append("")
        
        # Add dependencies with layout hints
        lines.append("' Dependencies")
        lines.append("skinparam maxMessageSize 60")
        
        # Group dependencies to reduce clutter
        for comp_name, comp_info in sorted(components.items()):
            deps = comp_info.get('dependencies', [])
            if deps:
                for dep in sorted(deps):
                    if dep in components:
                        lines.append(f'{self._sanitize_id(dep)} --> {self._sanitize_id(comp_name)}')
        
        lines.append("")
        lines.append("@enduml")
        
        return '\n'.join(lines)
    
    def generate_package_diagram(self, packages: List[str], dependencies: Dict) -> str:
        """Generate PlantUML package diagram"""
        lines = [
            "@startuml Package Dependencies",
            "!theme plain",
            "",
            "title Package Dependencies",
            ""
        ]
        
        # Add packages
        for pkg in sorted(packages):
            lines.append(f'package "{pkg}" {{')
            lines.append('}')
            lines.append("")
        
        # Add dependencies (simplified - would need more analysis)
        lines.append("@enduml")
        
        return '\n'.join(lines)
    
    def generate_architecture_diagram(self, components: Dict, api_spec: Dict) -> str:
        """Generate high-level architecture diagram"""
        lines = [
            "@startuml Architecture",
            "!theme plain",
            "skinparam linetype ortho",
            "skinparam packageStyle rectangle",
            "",
            "title Service Architecture",
            ""
        ]
        
        # Group components by type
        api_components = []
        service_components = []
        data_components = []
        other_components = []
        
        for comp_name, comp_info in components.items():
            name_lower = comp_name.lower()
            if 'handler' in name_lower or 'api' in name_lower or 'endpoint' in name_lower:
                api_components.append((comp_name, comp_info))
            elif 'service' in name_lower or 'business' in name_lower:
                service_components.append((comp_name, comp_info))
            elif 'repo' in name_lower or 'db' in name_lower or 'data' in name_lower:
                data_components.append((comp_name, comp_info))
            else:
                other_components.append((comp_name, comp_info))
        
        # API Layer
        if api_components:
            lines.append("package \"API Layer\" {")
            for comp_name, comp_info in api_components:
                display_name = comp_name if comp_name != 'root' else 'main'
                lines.append(f'  component "{display_name}" as {self._sanitize_id(comp_name)}')
            lines.append("}")
            lines.append("")
        
        # Service Layer
        if service_components:
            lines.append("package \"Service Layer\" {")
            for comp_name, comp_info in service_components:
                display_name = comp_name if comp_name != 'root' else 'main'
                lines.append(f'  component "{display_name}" as {self._sanitize_id(comp_name)}')
            lines.append("}")
            lines.append("")
        
        # Data Layer
        if data_components:
            lines.append("package \"Data Layer\" {")
            for comp_name, comp_info in data_components:
                display_name = comp_name if comp_name != 'root' else 'main'
                lines.append(f'  component "{display_name}" as {self._sanitize_id(comp_name)}')
            lines.append("}")
            lines.append("")
        
        # Other components
        if other_components:
            lines.append("package \"Other Components\" {")
            for comp_name, comp_info in other_components:
                display_name = comp_name if comp_name != 'root' else 'main'
                lines.append(f'  component "{display_name}" as {self._sanitize_id(comp_name)}')
            lines.append("}")
            lines.append("")
        
        # Dependencies between layers with layout optimization
        lines.append("' Layer Dependencies")
        lines.append("skinparam maxMessageSize 60")
        
        # Group dependencies to reduce visual clutter
        for comp_name, comp_info in components.items():
            deps = comp_info.get('dependencies', [])
            if deps:
                for dep in deps:
                    if dep in components:
                        lines.append(f'{self._sanitize_id(dep)} --> {self._sanitize_id(comp_name)}')
        
        # Add API endpoints info
        if api_spec.get('grpc') or api_spec.get('rest'):
            lines.append("")
            lines.append("note right")
            lines.append("  API Endpoints:")
            if api_spec.get('grpc'):
                lines.append(f"  gRPC: {len(api_spec['grpc'])} endpoints")
            if api_spec.get('rest'):
                lines.append(f"  REST: {len(api_spec['rest'])} endpoints")
            lines.append("end note")
        
        lines.append("")
        lines.append("@enduml")
        
        return '\n'.join(lines)
    
    def _sanitize_id(self, name: str) -> str:
        """Convert component name to valid PlantUML identifier"""
        # Replace special characters
        sanitized = name.replace('/', '_').replace('-', '_').replace('.', '_')
        # Remove leading numbers
        if sanitized and sanitized[0].isdigit():
            sanitized = 'c' + sanitized
        return sanitized or 'root'
