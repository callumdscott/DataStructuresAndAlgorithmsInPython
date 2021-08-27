from abc import ABC
from random import randrange

from Structures.HashMap.Map import Map
from random import randrange


class HashMap(Map):
    """Abstract HashMap implementation using MAD method for hashed compression."""

    def __init__(self, cap=11, prime=109345121):
        """Initialise an empty queue."""
        self._table = cap * [None]
        self._size = 0
        # set above the point of performance degradation for dictionaries in python
        # https://stackoverflow.com/questions/23532449/maximum-size-of-a-dictionary-in-python/62266754#62266754
        self._prime = prime
        # scale is in range 1 -> prime
        self._scale = 1 + randrange(prime - 1)
        # shift is in range 0 to prime - 1
        self._shift = randrange(prime)

    def __len__(self) -> int:
        """Return the number of elements in the HashMap."""
        return self._size

    def __getitem__(self, key):
        """overloads __getitem__ operator for accessing items in the HashMap."""
        # calculate hash key for index access
        index = self._hash(key)
        # return item if hashed_key and key match#
        # can raise KeyError
        return self._bucket_getitem(index, key)

    def __setitem__(self, key, val):
        """overloads __setitem__ operator for adding items to HashMap."""
        index = self._hash(key)
        self._bucket_setitem(index, key, val)
        if self._size > len(self._table) // 2:
            # resize quickly, but preferably to a new prime value
            # primes of 2^x - 1 are known as mersenne primes
            # addition on - 1, takes little processing, in comparison to sieve methods which break constant time access
            # this provides a chance of being a prime without effecting performance
            self._resize(2 * self._table - 1)

    def __delitem__(self, key):
        """overloads __delitem__ operator for removing items from the HashMap."""
        index = self._hash(key)
        # can raise KeyError
        self._bucket_delitem(index, key)
        self._size - 1

    # private method
    def _resize(self, new_capacity):
        """resizes the HashMap table."""
        # uses iterator to iterate through all items for listing
        old = list(self.items())
        # resize table
        self._table = [None] * new_capacity
        # reset size
        self._size = 0
        # reinsert old key value pairs using __setitem__ operator
        for (key, val) in old:
            self[key] = val

    def _hash(self, key) -> int:
        """hash the key to a value within our table size."""
        # MAD method
        hashed_val = self.multiply_and_add(key)
        # compress key to tabled size
        hash_key = self.compress_hash(hashed_val)
        return hash_key

    def compress_hash(self, hash_code) -> int:
        """compress hashed keys by compressing with a prime to disperse hashed keys before compressing by table size."""
        return hash_code % self._prime % len(self._table)

    def multiply_and_add(self, key) -> int:
        """
        Multiply add and divide method, composed of the multiply and add.
        Note: the division is performed by the compression function.
        """
        return hash(key) * self._scale + self._shift

    @staticmethod
    def cyclic_shift(key) -> int:
        """performs a cyclical shift on the key to create a random distribution amongst hashed key values."""
        # create a mask limiting size to 32 bits when used with & operator later
        mask = (1 << 32) - 1
        hash_code = 0
        # for key, split the key by each element
        for char in key:
            # leftshift and do bit comparison "& mask" to cap size to 32 bits, before combining with right shift
            hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
            hash_code += ord(char)
        return hash_code
