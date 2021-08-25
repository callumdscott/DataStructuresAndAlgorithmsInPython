from Errors.Empty import Empty
from Structures.LinkedLists.Node import Node


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_SIZE = 10

    def __init__(self):
        """Initialise an empty queue."""
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def first(self):
        """Returns the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.head.object_held

    def dequeue(self):
        """Returns and removes the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Stack is empty")
        current = self.head
        self.head = self.head.next
        return current.object_held

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        new_node = Node(e)
        # if the list is empty we also set the head
        if self.is_empty():
            self.head = new_node
        # else we set it to the tail
        else:
            self.tail.next = new_node
        # then we set tail to point to the last added
        self.tail = new_node
