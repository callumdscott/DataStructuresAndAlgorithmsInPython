class Node:
    """Node for storing data of Singly Linked Lists."""
    def __init__(self, object_to_hold):
        """Initialises a Node for Singly Linked Lists."""
        self.object_held = object_to_hold
        self.next = None