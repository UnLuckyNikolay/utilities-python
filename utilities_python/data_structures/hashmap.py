# pyright: reportOptionalSubscript=false

from collections.abc import Hashable
from typing import Any


class HashMapIsFullError(Exception):
    """Custom exception raised when object is being added to a full hashmap."""
    pass

class HashMap:
    """
    Stores objects as pairs of keys (Hashable) and values (Any).

    Methods
    -------
    - insert(key, value)
        Adds the value to the hashmap using the key.

        Raises `HashMapIsFullError` if `max_size` is set and hashmap is full.

    - get(key) -> Any
        Returns the value using the given key.

        Raises `KeyError` if the key isn't present in the hashmap.

    - pop(key) -> Any
        Removes and returns the value using the given key.

        Raises `KeyError` if the key isn't present in the hashmap.
    
    - get_size -> int
        Returns the amount of kvpairs in the hashmap.

    Raises
    ------
    - HashMapIsFullError
        If `max_size` is set and hashmap is full during `add`.

    - KeyError
        If the key isn't present in the hashmap during `get` or `pop`.
    """

    def __init__(self, default_size : int = 8, maximum_size : int = None): # pyright: ignore[reportArgumentType]
        if default_size <= 0 or (maximum_size != None and maximum_size <= 0):
            raise ValueError("Sizes must be positive integers.")
        if maximum_size != None and maximum_size < default_size:
            raise ValueError("Maximum size should be greater or equal to the default size.")
        
        self._hashmap = [None for i in range(default_size)]
        self._maximum_size = maximum_size

        self._resize_threshold = 0.3 # How full hashmap can be before it's resized
        self._resize_increase_mult = 2 # By how many times the hashmap is increased once threshold is met
        self._filled_buckets = 0 # Amount of filled slots

    def __repr__(self):
        result = ""
        for (index, value) in enumerate(self._hashmap):
            if value != None:
                result += f" - {index}: {value}\n"
        return result
    

    def insert(self, key : Hashable, value : Any):
        """
        Adds the value to the hashmap using the key.

        Raises `HashMapIsFullError` if `max_size` is set and hashmap is full.
        """
        
        self._resize()
        self._insert_inner(key, value)
        self._filled_buckets += 1

    def get(self, key : Hashable) -> Any:
        """
        Returns the value using the given key.

        Raises `KeyError` if the key isn't present in the hashmap.
        """

        index = self._key_to_index(key)
        original_index = index
        first_iteration = True

        while self._hashmap[index] != None:
            if self._hashmap[index][0] == key:
                return self._hashmap[index][1]
            if index == original_index and not first_iteration:
                raise KeyError(f"{key} is not present in the hashmap.")
            index = (index + 1) % len(self._hashmap)
            first_iteration = False
            
        raise KeyError(f"{key} is not present in the hashmap.")
    
    def pop(self, key : Hashable) -> Any:
        """
        Removes and returns the value using the given key.

        Raises `KeyError` if the key isn't present in the hashmap.
        """

        index = self._key_to_index(key)
        original_index = index
        first_iteration = True

        while self._hashmap[index] != None:
            if self._hashmap[index][0] == key:
                value = self._hashmap[index][1]
                self._hashmap[index] = None
                self._filled_buckets -= 1
                return value
            if index == original_index and not first_iteration:
                raise KeyError(f"{key} is not present in the hashmap.")
            index = (index + 1) % len(self._hashmap)
            first_iteration = False
            
        raise KeyError(f"{key} is not present in the hashmap.")
    
    def get_size(self) -> int:
        """Returns the amount of kvpairs in the hashmap."""

        return self._filled_buckets
    

    def _insert_inner(self, key : Hashable, value : Any):
        """Inner part of the insert method, also used during resizing to reinsert old pairs."""

        index = self._key_to_index(key)
        original_index = index
        first_iteration = True

        while (
            self._hashmap[index] != None
            and self._hashmap[index][0] != key
        ):
            if index == original_index and not first_iteration:
                raise HashMapIsFullError("HashMap has reached the maximum size.")
            index = (index + 1) % len(self._hashmap)
            first_iteration = False

        self._hashmap[index] = (key, value) # pyright: ignore
    
    def _resize(self):
        if len(self._hashmap) == 0:
            self._hashmap = [None]
            return
        if self._current_load() < self._resize_threshold:
            return # Size under the threshold
        if self._maximum_size != None and len(self._hashmap) >= self._maximum_size:
            return # Maximum size reached
        
        old_hashmap = self._hashmap
        if self._maximum_size == None:
            self._hashmap = [None] * (self._resize_increase_mult * len(old_hashmap))
        else:
            self._hashmap = [None] * min((self._resize_increase_mult * len(old_hashmap)), self._maximum_size)
        for kvpair in old_hashmap:
            if kvpair != None:
                self._insert_inner(kvpair[0], kvpair[1])

    def _current_load(self) -> float:
        if len(self._hashmap) == 0:
            return 1
        return self._filled_buckets/len(self._hashmap)

    def _key_to_index(self, key : Hashable) -> int:
        index = 0
        for c in key: # pyright: ignore[reportGeneralTypeIssues]
            index += ord(c)
        return index % len(self._hashmap)