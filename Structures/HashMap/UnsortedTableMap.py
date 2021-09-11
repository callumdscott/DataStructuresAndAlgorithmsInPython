from Structures.HashMap.Map import Map


class UnsortedTableMap(Map):
    """ Map using unordered list."""
    """"Code for HashMaps from Data Structures and Algorithms in Python, by Tamassia et. al, 2013"""
    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __getitem__(self, key):
        """returns a value from the table if the key has a match."""
        for item in self._table:
            if key == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(key))

    def __setitem__(self, key, value):
        """inserts an key-value Item into the table."""
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Removes a key-value Item into the table."""
        for index in range(len(self._taable)):
            if key == self._table[index]._key:
                self._table.pop(index)
                return
        raise KeyError('Key Error: ' + repr(key))

    def __len__(self) -> int:
        """Returns the len of the table."""
        return len(self._table)

    def __iter__(self):
        """ creates an iterable object from the table."""
        for item in self._table:
            yield item._key
