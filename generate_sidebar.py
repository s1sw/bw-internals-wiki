# Automatically generates the sidebar for the class reference
import os

class Namespace():
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.files = []

    def __str__(self):
        return f"Namespace({self.name}, children: {str(self.children)}, files: {str(self.files)})"

    def __repr__(self):
        return str(self)


def get_namespace_from_path(path_list):
    current = namespaces[path_list[0]]
    for el in path_list[1:]:
        current = current.children[el]
    return current

def create_namespaces():
    class_ref_dir = "docs" + os.sep + "class-reference"
    for root, dirs, files in os.walk(class_ref_dir):
        path = root.split(os.sep)[1:]

        last_namespace = None

        # Create necessary references
        for el in path:
            if last_namespace == None:
                if el not in namespaces:
                    namespaces[el] = Namespace(el)
                else:
                    last_namespace = namespaces[el]
            else:
                this_namespace = Namespace(el)
                last_namespace.children[el] = this_namespace
                last_namespace = this_namespace

        # Add files to namespaces
        for file in files:
            get_namespace_from_path(path).files.append("/" + "/".join(path) + "/" + file)

def generate_namespace_docs(namespace, indent_level = 1):
    global generated_str

    indent_str = "  " * indent_level
    for k, child in namespace.children.items():
        generated_str += indent_str + f"* {child.name}\n"
        generate_namespace_docs(child, indent_level + 1)

    for file in namespace.files:
        file_name = file.split("/")[-1].split(".")[0]
        generated_str += indent_str + f"* [{file_name}]({file})\n"

namespaces = {}

create_namespaces()

template_str = ""

with open("docs/_sidebar_template.md", "r") as template_file:
    template_str = template_file.read()

generated_str = "* Class Reference\n"

for k, v in namespaces.items():
    generate_namespace_docs(v)

generated_str = generated_str.strip()

template_str = template_str.replace("{{CLASS_REFERENCE}}", generated_str)

with open("docs/_sidebar.md", "w") as sidebar_file:
    sidebar_file.write(template_str)
