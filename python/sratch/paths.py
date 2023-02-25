from .tree import Tree

tree = Tree()
tree.create_node("/", "/")

def add_path(path):
    split = path.split("/")
    for i in range(len(split)):
        tree.create_node(i, i, parent="")