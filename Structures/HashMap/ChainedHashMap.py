from Structures.HashMap.HashMap import HashMap
from Structures.HashMap.UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMap):
    """Concrete implementation of a HashMap using chaining for collisions."""

    def _bucket_getitem(self, index, key):
        """returns an Item from the bucket if the hashed index and key match."""
        bucket = self._table[index]
        if bucket is None:
            # alert if no match is found
            raise KeyError('Key Error: ' + repr(key))
        # may raise key error if the bucket doesnt contain the right key
        return bucket[key]

    def _bucket_setitem(self, index, key, val):
        """inserts an key-value Item into the bucket."""
        if self._table[index] is None:
            self._table[index] = UnsortedTableMap()
        old_size = len(self._table[index])
        self._table[index][key] = val
        if len(self._table[index]) > old_size:
            self._size += 1

    def _bucket_delitem(self, index, key):
        """removes a key-value Item from the bucket if present."""
        bucket = self._table[index]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))
        del bucket[key]

    def __iter__(self):
        """creates an iterable from the table."""
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key
