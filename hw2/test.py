
import argparse
import zipfile
import xml.etree.ElementTree as ET
import os

def parse_nuspec(nuspec_file):
    tree = ET.parse(nuspec_file)
    root = tree.getroot()
    ns = {'ns': 'http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd'}
    
    dependencies = []
    for group in root.findall('.//ns:dependencies/ns:group', ns):
        target_framework = group.attrib.get('targetFramework', 'any')
        for dependency in group.findall('ns:dependency', ns):
            dep_id = dependency.attrib['id']
            dep_version = dependency.attrib.get('version', 'unknown')
            dependencies.append((dep_id, dep_version, target_framework))
    return dependencies

def extract_dependencies(package_path, depth, current_depth=0, target_framework='any'):
    if current_depth >= depth:
        return []

    dependencies = []
    with zipfile.ZipFile(package_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.nuspec'):
                with zip_ref.open(file) as nuspec_file:
                    package_dependencies = parse_nuspec(nuspec_file)
                    # Фильтруем зависимости по целевой платформе или берем все, если платформа 'any'
                    filtered_dependencies = [
                        (dep_id, dep_version) 
                        for dep_id, dep_version, framework in package_dependencies
                        if framework == target_framework or framework == 'any'
                    ]
                    for dep_id, dep_version in filtered_dependencies:
                        dependencies.append((dep_id, dep_version))
                        dep_path = f"{dep_id}.nupkg"  # Предполагается, что пакеты находятся локально
                        if os.path.exists(dep_path):
                            sub_dependencies = extract_dependencies(dep_path, depth, current_depth + 1, target_framework)
                            dependencies.extend(sub_dependencies)
    return dependencies

def visualize_graph(dependencies, output_file):
    with open(output_file, 'w') as f:
        f.write("digraph G {\n")
        for dep, sub_deps in dependencies:
            for sub_dep in sub_deps:
                f.write(f'    "{dep}" -> "{sub_dep}";\n')
        f.write("}\n")

def main():
    parser = argparse.ArgumentParser(description="Dependency Graph Visualizer")
    parser.add_argument("--graphviz-path", required=True, help="Path to Graphviz program")
    parser.add_argument("--package-name", required=True, help="Name of the package to analyze")
    parser.add_argument("--output-file", required=True, help="Path to output code file")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of dependency analysis")

    args = parser.parse_args()
    package_path = f"{args.package_name}.nupkg"

    if not os.path.exists(package_path):
        print(f"Package {package_path} not found.")
        return

    dependencies = extract_dependencies(package_path, args.max_depth)
    visualize_graph(dependencies, args.output_file)
    print(f"Graph code written to {args.output_file}")

if __name__ == "__main__":
    main()
