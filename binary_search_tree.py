class BSTTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTTreeNode(data)

    def inorder_traversal(self):
        elements = []

        # visit left
        # visit root
        # visit right

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()
        
        return elements

    def preorder_traversal(self):
        elements = []

        # visit root
        # visit left
        # visit right

        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []

        # visit left
        # visit right
        # visit root

        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def search(self, value):
        if value == self.data:
            print("Value Found!")
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

        

def build_bst(elements):
    root = BSTTreeNode(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_bst(numbers)

    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())

    print(tree.search(4))
