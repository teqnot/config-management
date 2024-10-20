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
    
    foo = parse_dependencies(dependencies)
    return foo

def parse_dependencies(deps):
    foo = {}
    for i in deps:
        if i[2] not in foo.keys():
            foo[i[2]] = {i[0] : i[1]}
        else:
            foo[i[2]][i[0]] = i[1]
    return foo

def extract_dependencies(package_path, depth, current_depth=0):
    if current_depth >= depth:
        return []
    dependencies = {}
    with zipfile.ZipFile(package_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.nuspec'):
                with zip_ref.open(file) as nuspec_file:
                    dependencies = parse_nuspec(nuspec_file)
    return dependencies

def visualize_graph(dependencies, output_file):
    with open(output_file, 'w') as f:
        f.write("digraph G {\n\tnode [shape=box];\n\n")
        print("digraph G {\n\tnode [shape=box];\n\n")
        for i in dependencies.keys():
            f.write(f'\t"{package_name}" -> "{i}";\n')
            print(f'\t"{package_name}" -> "{i}";\n')
            f.write(f'\tsubgraph "{i}"' + " {\n")
            print(f'\tsubgraph "{i}"' + " {\n")
            f.write(f'\t\tlabel="{i}";\n')
            print(f'\t\tlabel="{i}";\n')
            for j in dependencies[i]:
                f.write(f'\t\t"{i}" -> "{j}";\n')
                print(f'\t\t"{i}" -> "{j}";\n')
                f.write(f'\t\t"{j}" -> "{dependencies[i][j]}";\n')
                print(f'\t\t"{j}" -> "{dependencies[i][j]}";\n')
            f.write("\t}\n\n")
            print("\t}\n\n")
        f.write("}\n")
        print("}\n")

def main():
    global package_name
    parser = argparse.ArgumentParser(description="Dependency Graph Visualizer")
    parser.add_argument("--graphviz-path", required=True, help="Path to Graphviz program")
    parser.add_argument("--package-name", required=True, help="Name of the package to analyze")
    parser.add_argument("--output-file", required=True, help="Path to output code file")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of dependency analysis")

    args = parser.parse_args()
    package_name = args.package_name
    package_path = f"{args.package_name}.nupkg"

    if not os.path.exists(package_path):
        print(f"[ Package {package_path} not found ]")
        return

    dependencies = extract_dependencies(package_path, args.max_depth)
    visualize_graph(dependencies, args.output_file)
    print(f"[ Graph code written to {args.output_file} ]")

if __name__ == "__main__":
    main()
