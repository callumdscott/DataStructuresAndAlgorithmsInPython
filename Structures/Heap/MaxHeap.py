class MaxHeap:
    """MaxHeap for storing a max heap as a list."""
    """Implemented naiively from scratch without reference material."""

    def __init__(self, initial_list=None):
        """Initialises an empty MaxHeap, unless an initial list is present to build from."""
        self.heap = []
        if initial_list:
            self.build_heap(initial_list)

    def insert(self, item):
        """Appends an element to the bottom of the heap, sifting it up until the heap invariant is satisfied."""
        self.heap.append(item)
        self.sift_up(self.heap.len() - 1)

    def pop_max(self):
        """Pops the max value off of the heap, reorganising it to maintain the max heap invariant."""
        current_max = self.heap[0]
        self.heap[0], self.heap[self.heap.len() - 1] = self.heap[self.heap.len() - 1], self.heap[0]
        self.heap.pop()
        self.sift_down(0)
        return current_max

    def switch(self, index_a, index_b):
        """Generic switch method for swapping values at two indexes."""
        self.heap[index_a], self.heap[index_b] = self.heap[index_a], self.heap[index_b]

    def sift_up(self, index_pos):
        """Sifts an element up the array until it has no values smaller than it above itself."""
        if index_pos != 0:
            parent_pos = (index_pos - 1) // 2
            if self.head[index_pos] > self.heap[parent_pos]:
                self.switch(index_pos, parent_pos)
                self.sift_up(parent_pos)

    def is_empty(self):
        """Returns Boolean value of whether the MaxHeap is empty."""
        if len(self.heap) == 0:
            return True
        return False

    def sift_down(self, index_pos):
        """Sifts an element down the array until it has no values larger than it below itself."""
        left_index = 2 * index_pos + 1
        if left_index < self.heap.len() - 1:
            largest_index = left_index
            right_index = 2 * index_pos + 2
            if right_index < self.heap.len() - 1:
                if self.heap[right_index] > self.heap[left_index]:
                    largest_index = right_index
            if self.heap[largest_index] > self.heap[index_pos]:
                self.switch(index_pos, largest_index)
                self.sift_down(largest_index)

    def heap_sort(self, unordered_list):
        """Returns a list of sorted eleemnts from an unordered list using build_heap and pop_max."""
        self.build_heap(unordered_list)
        ordered_list = []
        while not self.is_empty():
            ordered_list.append(self.pop_max())
        return ordered_list

    def len(self):
        """Returns the length of the MaxHeap"""
        return len(self.heap)

    def build_heap(self, initial_list):
        """Builds a MaxHeap from a provided initial list in linear time."""
        n = (self.heap.len() - 1) / 2
        self.heap = initial_list
        for i in range(n, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, index_pos):
        """Recurusively builds a MaxHeap from previously smaller pairs of heap roots and the next node at index_pos"""
        left_index = 2 * index_pos + 1
        if left_index < self.heap.len() - 1:
            largest_index = left_index
            right_index = 2 * index_pos + 2
            if right_index < self.heap.len() - 1:
                if self.heap[right_index] > self.heap[left_index]:
                    largest_index = right_index
            if self.heap[largest_index] > self.heap[index_pos]:
                self.switch(index_pos, largest_index)