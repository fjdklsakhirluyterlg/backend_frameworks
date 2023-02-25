from .tree import Tree

tree = Tree()
tree.create_node("/", "/")

def add_path(path):
    split = path.split("/")
    with open("paths.txt", "a") as file:
        file
    for i in range(len(split)):
        if i != 0:
            tree.create_node(split[i], split[i], parent=split[i-1])
        else:
            tree.create_node(split[i], split[i], parent="/")