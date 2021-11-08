class MaxHeap:
    """MaxHeap for storing a max heap as a list."""
    """Implemented naiively from scratch without reference material"""
    # TODO: DOCUMENT
    # TODO: TEST

    def __init__(self, initial_list=None):
        self.heap = []
        if initial_list:
            self.build_heap(initial_list)

    def insert(self, item):
        self.heap.append(item)
        self.sift_up(self.heap.len() - 1)

    def pop_max(self):
        current_max = self.heap[0]
        self.heap[0], self.heap[self.heap.len() - 1] = self.heap[self.heap.len() - 1], self.heap[0]
        self.heap.pop()
        self.sift_down(0)
        return current_max

    def switch(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_a], self.heap[index_b]

    def sift_up(self, index_pos):
        if index_pos != 0:
            parent_pos = (index_pos - 1) // 2
            if self.head[index_pos] > self.heap[parent_pos]:
                self.switch(index_pos, parent_pos)
                self.sift_up(parent_pos)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False

    def sift_down(self, index_pos):
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

    def descending_heap_sort(self, unordered_list):
        self.build_heap(unordered_list)
        ordered_list = []
        while not self.is_empty():
            ordered_list.append(self.pop_max())
        return ordered_list

    def len(self):
        return len(self.heap)

    def build_heap(self, initial_list):
        n = (self.heap.len() - 1) / 2
        self.heap = initial_list
        for i in range(n, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, index_pos):
        left_index = 2 * index_pos + 1
        if left_index < self.heap.len() - 1:
            largest_index = left_index
            right_index = 2 * index_pos + 2
            if right_index < self.heap.len() - 1:
                if self.heap[right_index] > self.heap[left_index]:
                    largest_index = right_index
            if self.heap[largest_index] > self.heap[index_pos]:
                self.switch(index_pos, largest_index)