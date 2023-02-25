class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, obj):
        self.children.append(obj)