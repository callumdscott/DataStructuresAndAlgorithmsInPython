import math
import random


class Sort:

    def __init__(self, unsorted_list):
        self.list_elements = unsorted_list

    def selection_sort(self):
        for i in range(len(self.list_elements) - 1):
            min_index = i
            for x in range(i + 1, len(self.list_elements)):
                if self.list_elements[x] < self.list_elements[min_index]:
                    min_index = x
            if min_index != i:
                self.list_elements[min_index], self.list_elements[i] = self.list_elements[i], self.list_elements[
                    min_index]

    def insertion_sort(self):
        for i in range(len(self.list_elements)):
            count = i
            while count > 0 and self.list_elements[count] < self.list_elements[count - 1]:
                self.list_elements[count], self.list_elements[count - 1] = self.list_elements[count - 1], \
                                                                           self.list_elements[count]
                count -= 1

    def bubble_sort(self):
        for i in range(len(self.list_elements)):
            for j in range(len(self.list_elements) - 1):
                if self.list_elements[j] > self.list_elements[j + 1]:
                    self.list_elements[j], self.list_elements[j + 1] = self.list_elements[j + 1], self.list_elements[j]

    def merge_sort(self, in_place=False):
        if not in_place:
            self.list_elements = self.mergesort(self.list_elements)

    def mergesort(self, unordered_list):
        if len(unordered_list) == 2:
            if unordered_list[0] > unordered_list[1]:
                unordered_list[0], unordered_list[1] = unordered_list[1], unordered_list[0]
            return unordered_list
        elif len(unordered_list) > 2:
            split_index = len(unordered_list) // 2
            sorted_left = self.mergesort(unordered_list[:split_index])
            sorted_right = self.mergesort(unordered_list[split_index:])
            return self.merge(sorted_left, sorted_right)
        else:
            return unordered_list

    @staticmethod
    def merge(list_1, list_2):
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
        # TODO: implement quicksort
        pass


if __name__ == '__main__':
    unsorted = [10, 3, 5, 1, 2, 7, 8, 6, 4, 9]
    to_sort = unsorted
    new_sort = Sort(to_sort)
    # new_sort.selection_sort()
    # print(new_sort.list_elements)
    # new_sort.insertion_sort()
    # print(new_sort.list_elements)
    # new_sort.bubble_sort()
    # print(new_sort.list_elements)
    # new_sort.merge_sort()
    # print(new_sort.list_elements)
    new_sort.quick_sort()
    print(new_sort.list_elements)
