from Errors.Empty import Empty


class ArrayStack:
    """LIFO stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Initialise an empty stack."""
        self.stack = []

    def __len__(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def is_empty(self) -> bool:
        """Returns True if list is empty."""
        return len(self.stack) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.stack.append(e)

    def top(self) -> object:
        """Return the element at the top of the stack."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.stack[-1]

    def pop(self) -> object:
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.stack.pop()
