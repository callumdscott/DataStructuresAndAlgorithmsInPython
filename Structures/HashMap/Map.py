from collections import MutableMapping


class Map(MutableMapping):
    """creates the Abstract Class using non public _Item class"""

    class _Item:
        """Key-Value pair Item"""
        __slots__ = '_key', '_value'

        def __init__(self, key, val):
            """Creates key value pair Item"""
            self._key = key
            self._value = val

        def __eq__(self, other) -> bool:
            """Returns if equal"""
            return self._key == other._key

        def __ne__(self, other) -> bool:
            """Returns if not equal"""
            return not (self._key == other._key)

        def __lt__(self, other) -> bool:
            """Returns if less than"""
            return self._key < other._key

        def __gt__(self, other) -> bool:
            """Returns if greater than"""
            return self._key > other._key
