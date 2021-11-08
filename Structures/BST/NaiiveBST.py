class Node:
    """Node for storing data of Binary Search Tree."""
    """Implemented naiively from scratch without reference material
        - INTIALLY TESTED: insert and remove"""
    # TODO: DOCUMENT

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def traverse(self, depth):
        if self.left:
            self.left.traverse(depth + 1)
        print(f"depth: {depth}")
        print(self.data)
        if self.right:
            self.right.traverse(depth + 1)

    def clear_node(self):
        self.data = None
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, data):
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
        if data == self.data:
            print(f"removing {data}...")
            if self.left is None and self.right is None:
                if self.parent:
                    if self.parent.left is self:
                        self.parent.left = None
                    else:
                        self.parent.right = None
            elif self.left and self.right:
                print(f"left of current node: {self.left.data} \nright of current node: {self.right.data}")
                min_node = self.right.get_min_node()
                print(f"min node: {min_node.data}")
                if min_node.right:
                    print(f"has child on right")
                    min_node.right.parent = min_node.parent
                    min_node.parent.left = min_node.right
                if min_node.left:
                    print(f"has child on left")
                    min_node.left.parent = min_node.parent
                    min_node.parent.right = min_node.right
                else:
                    print(f"has child none")
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
        if self.parent:
            self.parent.delete_tree()
        else:
            self.clear_node()

    def is_in_tree(self, data):
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
        if self.parent:
            return 1 + self.parent.get_depth()
        else:
            return 0

    def get_min_node(self):
        if self.left:
            return self.left.get_min_node()
        else:
            return self

    def get_max_node(self):
        if self.right:
            return self.right.get_max_node()
        else:
            return self

    def get_successor_node(self):
        return self.parent

    def get_root_node(self):
        if self.parent:
            return self.parent.get_root()
        else:
            return self
