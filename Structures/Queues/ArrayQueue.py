from Errors.Empty import Empty


class ArrayQueue:
    """FIFO queue implementation using  a Singly Linked List."""
    DEFAULT_SIZE = 10

    def __init__(self):
        """Initialise an empty queue."""
        self.size = 0
        self.queue = [None] ** ArrayQueue.DEFAULT_SIZE
        self._front = 0
        pass

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return  self.size == 0

    def first(self) -> object:
        """Returns the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Empty Queue")
        return self.data[self._front]

    def dequeue(self) -> object:
        """Returns and removes the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Empty Queue")
        element = self.queue[self._front]
        self.queue[self._front] = None
        self._front = (self._front + 1) % len(self.queue)
        self.size -= 1
        if 0 < self.size < len(self.queue) // 4:
            self.resize(len(self.queue)) // 2
        return element

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self.size == self.queue:
            self.resize(2 * len(self.queue))
        index_pos = (self.size + self._front) % len(self.queue)
        self.queue[index_pos] = e
        self.size += 1

    def resize(self, cap):
        """Resize the queue to a capacity greater than the current length."""
        old = self.queue
        self.queue = [None] * cap
        start = self._front
        for k in range(self.size):
            self.queue[k] = old[start]
            start = (start + 1) % len(self.queue)
        self._front = 0
