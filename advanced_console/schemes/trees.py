from ..colors import color_str

from .nodes import BaseNode


class _BaseTree:
    def __init__(self): pass
    def render(self): pass
    def display(self): pass


class ClassicVerticalTree(_BaseTree):
    def __init__(self, root_node: BaseNode):
        super().__init__()

        self.root = root_node

    def render(self, colored: bool = False):
        lines = []

        def _render_node(node, prefix="", is_last=True):
            line = \
                f"{prefix}{'└── ' if is_last else '├── '}{color_str(node.name, node.color) if colored else node.name}"
            lines.append(line)

            new_prefix = prefix + ("    " if is_last else "│   ")
            for i_, child_ in enumerate(node.children):
                _render_node(child_, new_prefix, i_ == len(node.children) - 1)

        # Root line (without ├──)
        lines.append(f"{color_str(self.root.name, self.root.color) if colored else self.root.name}")
        for i, child in enumerate(self.root.children):
            _render_node(child, "", i == len(self.root.children) - 1)
        return "\n".join(lines)

    def display(self):
        print(self.render(colored=True))

    def save_on_file(self, filename: str):
        with open(file=str(filename), mode="w", encoding="UTF-8") as file:
            file.write(self.render(colored=False))
