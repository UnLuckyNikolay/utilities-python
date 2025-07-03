from typing import Any


class LListIsEmptyError(Exception):
    """Custom exception raised when `pop_*` or `peek_*` operation is performed on an empty linked list."""
    pass

class LListIsFullError(Exception):
    """Custom exception raised when `add_*` operation is performed on a full linked list."""
    pass

class LinkedList:
    """
    Collection of nodes with references to the next one.

    Methods
    -------
    - add_to_tail(object)
        Add object to the end of the linked list.

    - add_to_head(object)
        Add object to the start of the linked list.

    - pop_from_head -> Any | None
        Removes and returns the item from the head of the linked list.
        Returns `None`/raises `LListIsEmptyError` if linked list is empty, depending on `raise_errors_on_empty_op`.

    - peek_from_head -> Any | None
        Returns the item from the head without removing it.
        Returns `None`/raises `LListIsEmptyError` if linked list is empty, depending on `raise_errors_on_empty_op`.

    - size -> int
        Returns the size of the linked list.

    - is_empty -> bool
        Returns `True` if linked list is empty, otherwise `False`.

    - is_full -> bool
        Returns `True` if `max_size` is set and the linked list is full, otherwise `False`.
         
    Raises
    ------
    - LListIsFullError
        If `max_size` is set and `add_*` is performed when size of the linked list equals `max_size`.

    - LListIsEmptyError
        If `raise_errors_on_empty_op` is set to `True` and `peek_*`/`pop_*` is performed on an empty linked list.
    """
    def __init__(self, max_size: int = None, raise_errors_on_empty_op : bool = False):
        """
        Args
        ----
        - max_size : int, optional
            Maximum size of the linked list. 
            (default = None)

        - raise_errors_on_empty_op : bool, optional
            Changes `peek_*`/`pop_*` to raise errors if the linked list is empty instead of returning `None`.
            (default = False)
        """
        self._head = None
        self._tail = None
        self._size = 0
        self._max_size = max_size
        self._raise_errors_on_empty_op = raise_errors_on_empty_op

    def __repr__(self):
        values = []
        current = self._head
        while current:
            values.append(str(current._val))
            current = current._next
        text = " -> ".join(values)
        return f"[{text}]"
    
    def __iter__(self):
        node = self._head
        while node != None:
            yield node
            node = node._next


    def add_to_tail(self, object : Any):
        """Add object to the end of the linked list."""
        if self._max_size != None and self._size >= self._max_size:
            raise LListIsFullError("Cannot push to a full linked list.")

        new_node = _Node(object)
        if self._head != None:
            self._tail.set_next(new_node)
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def add_to_head(self, object : Any):
        """Add object to the start of the linked list."""
        if self._max_size != None and self._size >= self._max_size:
            raise LListIsFullError("Cannot push to a full linked list.")
        
        new_node = _Node(object)
        if self._head != None:
            new_node.set_next(self._head)
        else:
            self._tail = new_node
        self._head = new_node
        self._size += 1

    def pop_from_head(self) -> Any:
        if self._head == None:
            if self._raise_errors_on_empty_op:
                raise LListIsEmptyError("Cannot pop from an empty linked list.")
            return None
        
        node = self._head
        if self._head == self._tail:
            self._tail = None
        self._head = self._head._next
        self._size -= 1
        return node._val
    
    def peek_from_head(self) -> Any:
        if self._head == None:
            if self._raise_errors_on_empty_op:
                raise LListIsEmptyError("Cannot pop from an empty linked list.")
            return None
        
        return self._head._val
    
    def size(self) -> int:
        """Returns the size of the linked list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Returns `True` if linked list is empty, otherwise `False`."""
        return self._size == 0

    def is_full(self) -> bool:
        """Returns `True` if `max_size` is set and the linked list is full, otherwise `False`."""
        return self._max_size != None and self._size >= self._max_size


class _Node:
    """
    Internal class for the Linked List.
    """
    def __init__(self, val):
        self._val = val
        self._next = None

    def __repr__(self):
        return self._val


    def set_next(self, node):
        self._next = node