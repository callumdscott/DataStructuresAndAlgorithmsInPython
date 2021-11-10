class Node:
    """Node for storing data of Binary Search Tree."""
    """Implemented naiively from scratch without reference material"""

    def __init__(self, data):
        """Initialises an empty Binary Search Tree."""
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def traverse(self, depth):
        """Prints the contents of the Binary Search Tree, using an in-order traversal."""
        if self.left:
            self.left.traverse(depth + 1)
        print(f"depth: {depth}")
        print(self.data)
        if self.right:
            self.right.traverse(depth + 1)

    def clear_node(self):
        """clears the current node of any present data."""
        self.data = None
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, data):
        """Recursively adds an object with implemented comparison operators to the Binary Search Tree."""
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                self.right.parent = self

    def get_height(self):
        """Recursively counts the max height from a leaf node in the Binary Search Tree."""
        if self.left:
            left_count = 1 + self.left.get_height()
        else:
            left_count = 0
        if self.left:
            right_count = 1 + self.left.get_height()
        else:
            right_count = 0
        return max(left_count, right_count)

    def remove(self, data):
        """Removes a node from the Binary Search Tree if it is equivalent to the data arg."""
        if data == self.data:
            if self.left is None and self.right is None:
                if self.parent:
                    if self.parent.left is self:
                        self.parent.left = None
                    else:
                        self.parent.right = None
            elif self.left and self.right:
                min_node = self.right.get_min_node()
                if min_node.right:
                    min_node.right.parent = min_node.parent
                    min_node.parent.left = min_node.right
                if min_node.left:
                    min_node.left.parent = min_node.parent
                    min_node.parent.right = min_node.right
                else:
                    if min_node.parent.right == min_node:
                        min_node.parent.right = None
                    else:
                        min_node.parent.left = None
                self.data = min_node.data
            else:
                if self.left:
                    self.left.parent = self.parent
                    self.parent.left = self.left
                else:
                    self.left.parent = self.parent
                    self.parent.left = self.right
            return True
        elif data < self.data:
            if self.left:
                self.left.remove(data)
            else:
                return False
        else:
            if self.right:
                self.right.remove(data)
            else:
                return False

    def get_node_count(self):
        """Returns the total count of the number of nodes within the tree from the specified node, self inclusively."""
        if self.left is None and self.right is None:
            return 1
        elif self.left and self.right:
            return 1 + self.left.get_node_count() + self.right.get_node_count()
        else:
            if self.left:
                return 1 + self.left.get_node_count()
            else:
                return 1 + self.right.get_node_count()

    def delete_tree(self):
        """Recursively traverses the Node to the root of the Tree, where the node at the root is set to None."""
        if self.parent:
            self.parent.delete_tree()
        else:
            self.clear_node()

    def is_in_tree(self, data):
        """Returns Boolean value of whether the data is in the Binary Search Tree."""
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                self.left.is_in_tree(data)
            else:
                return False
        else:
            if self.right:
                self.right.is_in_tree(data)
            else:
                return False

    def get_depth(self):
        """Calculates the depth of the tree from its root."""
        if self.parent:
            return 1 + self.parent.get_depth()
        else:
            return 0

    def get_min_node(self):
        """Returns the left-most value of the Binary Search Tree."""
        if self.left:
            return self.left.get_min_node()
        else:
            return self

    def get_max_node(self):
        """Returns the right-most value of the Binary Search Tree."""
        if self.right:
            return self.right.get_max_node()
        else:
            return self

    def get_successor_node(self):
        """Returns the parent of the current Node."""
        return self.parent

    def get_root_node(self):
        """Recursively traverses the Node to the root of the Tree."""
        if self.parent:
            return self.parent.get_root()
        else:
            return self
