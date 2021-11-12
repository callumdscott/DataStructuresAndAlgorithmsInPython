import math
import random


class Sort:
    """Sort for storing a list to be ordered."""
    """Implemented naiively from scratch without reference material"""

    def __init__(self, unsorted_list):
        """Initialises a Sort class.
           Future Extension: allow for automated optimal sorting method to be used when called."""
        self.list_elements = unsorted_list

    def selection_sort(self):
        """Sorts list using selection sort algorithm."""
        for i in range(len(self.list_elements) - 1):
            min_index = i
            for x in range(i + 1, len(self.list_elements)):
                if self.list_elements[x] < self.list_elements[min_index]:
                    min_index = x
            if min_index != i:
                self.list_elements[min_index], self.list_elements[i] = self.list_elements[i], self.list_elements[
                    min_index]

    def insertion_sort(self):
        """Sorts list using insertion sort algorithm."""
        for i in range(len(self.list_elements)):
            count = i
            while count > 0 and self.list_elements[count] < self.list_elements[count - 1]:
                self.list_elements[count], self.list_elements[count - 1] = self.list_elements[count - 1], \
                                                                           self.list_elements[count]
                count -= 1

    def bubble_sort(self):
        """Sorts list using bubble sort algorithm."""
        for i in range(len(self.list_elements)):
            for j in range(len(self.list_elements) - 1):
                if self.list_elements[j] > self.list_elements[j + 1]:
                    self.list_elements[j], self.list_elements[j + 1] = self.list_elements[j + 1], self.list_elements[j]

    def merge_sort(self, in_place=False):
        """Sorts list using merge sort algorithm."""
        if not in_place:
            self.list_elements = self._mergesort(self.list_elements)

    def _mergesort(self, unordered_list):
        """Sorts list using internal mergesort method for recursive calls."""
        if len(unordered_list) == 2:
            if unordered_list[0] > unordered_list[1]:
                unordered_list[0], unordered_list[1] = unordered_list[1], unordered_list[0]
            return unordered_list
        elif len(unordered_list) > 2:
            split_index = len(unordered_list) // 2
            sorted_left = self._mergesort(unordered_list[:split_index])
            sorted_right = self._mergesort(unordered_list[split_index:])
            return self.merge(sorted_left, sorted_right)
        else:
            return unordered_list

    @staticmethod
    def merge(list_1, list_2):
        """Merges two sorted list into a single sorted list."""
        new_list = []
        list_1_index = 0
        list_2_index = 0
        while list_1_index < len(list_1) and list_2_index < len(list_2):
            if list_1[list_1_index] <= list_2[list_2_index]:
                new_list.append(list_1[list_1_index])
                list_1_index += 1
            else:
                new_list.append(list_2[list_2_index])
                list_2_index += 1
        if list_1_index == len(list_1):
            new_list.extend(list_2[list_2_index:])
        else:
            new_list.extend(list_1[list_1_index:])
        return new_list

    def quick_sort(self):
        """Sorts list using quick sort algorithm."""
        random.shuffle(self.list_elements)
        self.list_elements = self._quicksort(self.list_elements)

    def _quicksort(self, unordered_list):
        """Sorts list using internal quicksort method for recursive calls."""
        if len(unordered_list) <= 1:
            return unordered_list
        pivot = unordered_list[0]
        less, equal, greater = self.partition(unordered_list, pivot)
        return self._quicksort(less) + equal + self._quicksort(greater)

    @staticmethod
    def partition(unordered_list, pivot):
        """Partitions an unordered list into 3 lists of elements less, more and equal to the pivot."""
        less, equal, greater = [], [], []
        for val in unordered_list:
            if val < pivot:
                less.append(val)
            if val == pivot:
                equal.append(val)
            if val > pivot:
                greater.append(val)
        return less, equal, greater
