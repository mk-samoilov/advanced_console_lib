class BaseNode:
    def __init__(self, name: str, color: str = "white"):
        self.name = str(name)
        self.color = color

        self.children = []

    def add(self, child_node):
        self.children.append(child_node)
