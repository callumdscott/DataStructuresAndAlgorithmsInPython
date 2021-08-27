from Errors.Empty import Empty
from Structures.LinkedLists.Node import Node


class LinkStack:
    """LIFO stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Initialise an empty stack."""
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        """Return the size of the stack."""
        return self.size

    def is_empty(self) -> bool:
        """Returns True if list is empty."""
        return self.size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.size += 1
        previous_head = self.head
        self.head = Node(e, previous_head)

    def top(self) -> object:
        """Return the element at the top of the stack."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.head.object_held

    def pop(self) -> object:
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise Empty("Stack is empty")
        current = self.head
        self.head = self.head.next
        self.size -= 1
        return current.object_held
