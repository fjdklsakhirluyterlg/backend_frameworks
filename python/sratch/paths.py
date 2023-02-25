from .tree import Tree

tree = Tree()
tree.create_node()

def add_path(path):
    split = path.split("/")
    for u in split:
        tree.create_node(u, u)