class Node:
    """Node for storing data of Binary Search Tree."""

    def __init__(self, data, parent=None, left=None, right=None):
        """Initialises a Node for Binary Search Tree."""
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """Adds an object with implemented comparison operators to the Binary Search Tree."""
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:

                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def min_value(self):
        """Prints the min value of the Binary Search Tree."""
        if self.left:
            return self.left.min_value()
        else:
            return self

    def max_value(self):
        """Prints the max value of the Binary Search Tree."""
        if self.right:
            return self.right.max_value()
        else:
            return self

    def inorder(self):
        """Prints the contents of the Binary Search Tree in order, smallest to largest."""
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self):
        """Prints the contents of the Binary Search Tree by starting at the root downwards, firstly left then right."""
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        """Prints the contents of the Binary Search Tree in by the left first, then the parent, then the right."""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
