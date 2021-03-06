from Structures.LinkedLists.Node import Node


class SinglyLinkedList:
    """Singly Linked List using Node Object for storage."""
    def __init__(self, head=None):
        """Initialises an empty Linked List."""
        self.count = 0
        self.head = None

    def append(self, object_item: object):
        """Adds an object inheriting from the object base class to the Linked List."""
        node = Node(object_item)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.count += 1

    def size(self) -> int:
        """Returns the size of the Linked List."""
        return self.count

    def empty(self) -> bool:
        """Returns True if the hte head pointer is set to None."""
        return True if self.head is None else False

    def item_at(self, index: int) -> int:
        """"Returns the item at index, based on 0 indexing."""
        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        return current.object_held

    def push_front(self, object_to_push_front: object):
        """Adds an element to the front of the Linked List."""
        node = Node(object_to_push_front)
        temp = self.head
        self.head = node
        self.head.next = temp

    def pop_front(self) -> int:
        """Returns and removes the object at the front of the Linked List."""
        temp = self.head
        self.head = self.head.next
        return temp.object_held

    def push_back(self, object_to_hold: object):
        """Adds object to the back of the Linked List."""
        node = Node(object_to_hold)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def pop_back(self) -> int:
        """Returns and removes the object at the back of the Linked List."""
        if not self.head:
            return None
        elif self.size() == 1:
            object_held = self.head.object_held
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            object_held = current.next.object_held
            current.next = None
            pass
        return object_held

    def front(self) -> int:
        """Returns the object at the front of the Linked List."""
        if self.head:
            return self.head.object_held
        return None

    def back(self) -> int:
        """Returns the object at the back of the Linked List."""
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            return current.object_held
        return None

    def insert(self, index: int, object_to_hold: object):
        """inserts an object at the index position of the Linked List."""
        current = self.head
        index -= 1
        while index > 0:
            current = current.next
            index -= 1
        temp1 = current.next
        current.next = Node(object_to_hold)
        current.next.next = temp1

    def erase(self, index: int):
        """Removes an object at the index position of the Linked List."""
        if index == 0:
            self.head = self.head.next
        else:
            index -= 1
            current = self.head
            while index > 0:
                current = current.next
                index -= 1
            if current.next.next is not None:
                current.next = current.next.next
            else:
                current.next = None

    def reverse(self):
        """Removes an object at the index position of the Linked List."""
        if self.head and self.head.next:
            previous = self.head
            next_item = self.head.next
            previous.next = None
            while next_item:
                new_next = next_item.next
                next_item.next = previous
                previous = next_item
                next_item = new_next
            self.head = previous
