from Structures.BST.Node import Node


class BinarySearchTree:
    """Binary Search Tree class acts as a Facade for a Binary Search Tree implementation using Nodes."""

    def __init__(self, root=None):
        """Initialises an empty Binary Search Tree."""
        self.root = root

    def insert(self, data):
        """Adds an object with implemented comparison operators to the Binary Search Tree."""
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def inorder(self):
        """Prints the contents of the Binary Search Tree in order, smallest to largest."""
        if self.root:
            self.root.inorder()

    def preorder(self):
        """Prints the contents of the Binary Search Tree by starting at the root downwards, firstly left then right."""
        if self.root:
            self.root.preorder()

    def postorder(self):
        """Prints the contents of the Binary Search Tree in by the left first, then the parent, then the right."""
        if self.root:
            self.root.postorder()

    def min_value(self):
        """Prints the min value of the Binary Search Tree."""
        if self.root:
            min_node = self.root.min_value()
        else:
            min_node = None
        print(min_node.data)

    def max_value(self):
        """Prints the max value of the Binary Search Tree."""
        if self.root:
            max_node = self.root.max_value()
        else:
            max_node = None
        print(max_node.data)

if __name__ == '__main__':
    tree = BinarySearchTree()
    print("Testing Insert: 14")
    tree.insert(50)
    tree.print_tree()
    print()
    print("Testing Insert: 23, 7")
    tree.insert(34)
    tree.insert(69)
    tree.print_tree()
    print()
    print("Testing Insert: 3, 11")
    tree.insert(20)
    tree.insert(45)
    tree.print_tree()
    print()
    print("Testing Insert: 9, 37")
    tree.insert(56)
    tree.insert(84)
    tree.print_tree()
    print()
    print("Testing in-order:")
    tree.inorder()
    print()
    print("Testing pre-order:")
    tree.preorder()
    print()
    print("Testing post-order:")
    tree.postorder()
    print()
    print("Min:")
    tree.min_value()
    print()
    print("Max:")
    tree.max_value()
