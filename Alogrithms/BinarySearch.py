class BinarySearch:
    """Binary Search class implementation for Lists."""

    def __init__(self, low=0, high=0, dataset=None):
        """Creates a binary search object."""
        self.low = low
        self.high = high
        self.mid = self.low + ((self.high - self.low) // 2)
        self.dataset = dataset

    def find_nearest_val(self, val):
        """Finds Value closest to the target val"""
        pass

    def find_val(self, val):
        """Returns True if value is present"""
        pass

    def find_first(self, val):
        """Returns index of the first occurrence of target val"""
        pass

    def find_last(self, val):
        """Returns index of the last occurrence of target val"""
        pass

    def find_all(self, val):
        """Returns index of the first and last occurrence of target val"""
        pass

    def find_insert_pos(self, val):
        """Returns the index position to insert a target val"""
        pass

    def insert(self, val):
        """Inserts the target val in the list, maintaining order"""
        pass

    def insert_n_times(self, val, n):
        """Inserts the target val in the list n times, maintaining order"""
        pass

    def any_within_variance(self, val, variance):
        """Returns a list of values in the target range, +- variance"""
        pass

    def find_values_in_range(self, low, high):
        """Returns a list of values in the range low - high"""
        pass
