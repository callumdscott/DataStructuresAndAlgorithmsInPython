class BinarySearch:
    """Binary Search class implementation for Lists."""

    def __init__(self, dataset):
        """Creates a binary search object."""
        self.low = 0
        self.high = len(dataset) - 1
        self.mid = self.low + ((self.high - self.low) // 2)
        self.dataset = dataset

    def find_nearest_val(self, val) -> [int, int]:
        """Finds value and index tuple closest to the target val"""
        # self.mid will point to the index position where to insert the val, ie. val larger than index val
        while self.low <= self.high:
            if self.dataset[self.mid] == val:
                return val, self.mid
            elif self.dataset[self.mid] > val:
                self.high = self.mid - 1
            else:
                self.low = self.mid + 1
            self.mid = self.low + ((self.high - self.low) // 2)
        # if mid is the last element we have found the closest value
        if self.mid == len(self.dataset) - 1:
            return self.dataset[-1], len(self.dataset) - 1
        # find the differences between the target and the values either side of it's place in the list
        difference_at_mid = abs(self.dataset[self.mid] - val)
        difference_next = abs(self.dataset[self.mid + 1] - val)
        # test if the previous or the current position has the closest value to our target
        if difference_at_mid <= difference_next:
            return self.dataset[self.mid], self.mid
        else:
            return self.dataset[self.mid + 1], self.mid + 1

    def find_val(self, val):
        """Returns True if value is present"""
        while self.low <= self.high:
            if self.dataset[self.mid] == val:
                return True
            elif self.dataset[self.mid] > val:
                self.high = self.mid - 1
            else:
                self.low = self.mid + 1
            self.mid = self.low + ((self.high - self.low) // 2)
        return False