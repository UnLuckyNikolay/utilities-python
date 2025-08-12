from typing import Any


class LLQueueIsEmptyError(Exception):
    """Custom exception raised when `pop` or `peek` operation is performed on an empty llqueue."""
    pass

class LLQueueIsFullError(Exception):
    """Custom exception raised when `push` operation is performed on a full llqueue."""
    pass

class LLQueue:
    """
    Abstract data structure. First in, first out. Linked List used to store items.
    Complexity of all methods - O(1).

    Methods
    -------
    - push(item)
        Add item to the end of the llqueue.
        Raises `LLQueueIsFullError` if `max_size` is set and size of the llqueue equals `max_size`.

    - pop -> Any | None
        Removes and returns the item from the head of the llqueue.
        Returns `None`/raises `LLQueueIsEmptyError` if llqueue is empty, depending on `raise_errors_on_empty_op`.

    - peek -> Any | None
        Returns the item from the head without removing it.
        Returns `None`/raises `LLQueueIsEmptyError` if llqueue is empty, depending on `raise_errors_on_empty_op`.

    - size -> int
        Returns the size of the llqueue.

    - is_empty -> bool
        Returns `True` if llqueue is empty, otherwise `False`.

    - is_full -> bool
        Returns `True` if `max_size` is set and the llqueue is full, otherwise `False`.
         
    Raises
    ------
    - LLQueueIsFullError
        If `max_size` is set and `add_*` is performed when size of the llqueue equals `max_size`.

    - LLQueueIsEmptyError
        If `raise_errors_on_empty_op` is set to `True` and `peek_*`/`pop_*` is performed on an empty llqueue.
    """

    def __init__(self, max_size: int = None, raise_errors_on_empty_op : bool = False):
        """
        Args
        ----
        - max_size : int, optional
            Maximum size of the llqueue. 
            (default = None)

        - raise_errors_on_empty_op : bool, optional
            Changes `peek_*`/`pop_*` to raise errors if the llqueue is empty instead of returning `None`.
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
        text = " <- ".join(values)
        return f"LLQueue[{text}]"
    
    def __iter__(self):
        node = self._head
        while node != None:
            yield node
            node = node._next


    def push(self, object : Any):
        """
        Add object to the end of the llqueue.

        Raises `LLQueueIsFullError` if `max_size` is set and size of the llqueue equals `max_size`.
        """

        if self._max_size != None and self._size >= self._max_size:
            raise LLQueueIsFullError("Cannot push to a full llqueue.")

        new_node = _Node(object)
        if self._head != None:
            self._tail.set_next(new_node)
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def pop(self) -> Any:
        """
        Removes and returns the item from the head of the llqueue.

        Returns `None`/raises `LLQueueIsEmptyError` if llqueue is empty, depending on `raise_errors_on_empty_op`.
        """

        if self._head == None:
            if self._raise_errors_on_empty_op:
                raise LLQueueIsEmptyError("Cannot pop from an empty llqueue.")
            return None
        
        node = self._head
        if self._head == self._tail:
            self._tail = None
        self._head = self._head._next
        self._size -= 1
        return node._val
    
    def peek(self) -> Any:
        """
        Returns the item from the head without removing it.

        Returns `None`/raises `LLQueueIsEmptyError` if llqueue is empty, depending on `raise_errors_on_empty_op`.
        """

        if self._head == None:
            if self._raise_errors_on_empty_op:
                raise LLQueueIsEmptyError("Cannot pop from an empty llqueue.")
            return None
        
        return self._head._val
    
    def size(self) -> int:
        """Returns the size of the llqueue."""

        return self._size
    
    def is_empty(self) -> bool:
        """Returns `True` if llqueue is empty, otherwise `False`."""

        return self._size == 0

    def is_full(self) -> bool:
        """Returns `True` if `max_size` is set and the llqueue is full, otherwise `False`."""
        
        return self._max_size != None and self._size >= self._max_size


class _Node:
    """Internal class for the llqueue."""
    
    def __init__(self, val):
        self._val = val
        self._next = None

    def __repr__(self):
        return self._val


    def set_next(self, node):
        self._next = node