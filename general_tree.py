class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child: TreeNode):
        child.parent = self
        self.children.append(child)


    def get_level(self):
        parentCount = 0

        current = self
        while current.parent:
            current = current.parent
            parentCount += 1
            
        return parentCount

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = "|__" if self.parent else ""
        print(f"{spaces}{prefix} {self.data}")

        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_electronic_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Motorolla"))

    television = TreeNode("Television")
    television.add_child(TreeNode("LG"))
    television.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(television)

    return root

if __name__ == "__main__":
    root = build_electronic_tree()
    root.print_tree()

    print()
    print(root.get_level())
    pass
