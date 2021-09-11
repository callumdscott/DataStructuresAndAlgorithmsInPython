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

    def delete_node(self, data):
        """ deletes the node if the data is present within the tree structure."""
        if self.data == data:
            if self.right and self.left:
                [parent_successor, successor] = self.right.get_min(self)
                if parent_successor.left == successor:
                    parent_successor.left = successor.right
                else:
                    parent_successor.right = successor.right
                successor.left = self.left
                successor.right = self.right
                return successor
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.data > data:
                if self.left:
                    self.left = self.left.delete_node(data)
            else:
                if self.right:
                    self.right = self.right.delete_node(data)

        return self

    def get_min(self, parent):
        """ return the minimum node in the current tree and its parent."""
        if self.left:
            return self.left.get_min(self)
        else:
            return [parent, self]