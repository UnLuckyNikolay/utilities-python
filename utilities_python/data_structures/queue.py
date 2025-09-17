from typing import Any


class QueueIsEmptyError(Exception):
    """Custom exception raised when pop or peek operation is performed on an empty queue."""
    pass

class QueueIsFullError(Exception):
    """Custom exception raised when push operation is performed on a full queue."""
    pass

class Queue:
    """
    Abstract data structure. First in, first out.
    Complexity of `pop` - O(n), the rest - O(1).

    Methods
    -------
    - push(item)
        Puts an item at the tail of the queue.

    - pop -> Any | None
        Removes and returns the item from the head of the queue.
        Returns `None`/raises `QueueIsEmptyError` if queue is empty, depending on `raise_errors_on_empty_op`.

    - peek -> Any | None
        Returns the item from the head without removing it.
        Returns `None`/raises `QueueIsEmptyError` if queue is empty, depending on `raise_errors_on_empty_op`.

    - size -> int
        Returns the size of the queue.

    - is_empty -> bool
        Returns `True` if queue is empty, otherwise `False`.

    - is_full -> bool
        Returns `True` if `max_size` is set and the queue is full, otherwise `False`.

    Raises
    ------
    - QueueIsFullError
        If `max_size` is set and `push` is performed when size of the queue equals `max_size`.

    - QueueIsEmptyError
        If `raise_errors_on_empty_op` is set to `True` and `peek`/`pop` is performed on an empty queue.
    """
    
    def __init__(self, max_size: int = None, raise_errors_on_empty_op: bool = False): # pyright: ignore[reportArgumentType]
        """
        Args
        ----
        - max_size : int, optional
            Maximum size of the queue. 
            (default = None)

        - raise_errors_on_empty_op : bool, optional
            Changes `peek`/`pop` to raise errors if the queue is empty instead of returning `None`.
            (default = False)
        """
        self._items = []
        self._max_size = max_size
        self._raise_errors_on_empty_op = raise_errors_on_empty_op

    def __repr__(self):
        return f"Queue{self._items}"

    def __iter__(self):
        return self._items
    
    def __eq__(self, other):
        if not isinstance(other, Queue):
            return False
        
        if self.size() != other.size():
            return False
        
        for i in range(0, self.size()):
            if self._items[i] != other._items[i]:
                return False
            
        return True
    
    def __len__(self):
        return len(self._items)


    def push(self, item: Any):
        """
        Puts an item at the tail of the queue.
        
        Raises `QueueIsFullError` if `max_size` is set and size of the queue equals `max_size`.
        """
        if self._max_size != None and self.size() >= self._max_size:
            raise QueueIsFullError("Cannot push to a full queue.")
        self._items.append(item)

    def pop(self) -> Any | None:
        """
        Removes and returns the item from the head of the queue.
        
        Returns `None`/raises `QueueIsEmptyError` if queue is empty, depending on `raise_errors_on_empty_op`.
        """
        if len(self._items)==0:
            if self._raise_errors_on_empty_op:
                raise QueueIsEmptyError("Cannot pop from an empty queue.")
            return None
        item = self._items.pop(0)
        return item

    def peek(self) -> Any | None:
        """
        Returns the item from the head without removing it.

        Returns `None`/raises `QueueIsEmptyError` if queue is empty, depending on `raise_errors_on_empty_op`.
        """
        if len(self._items)==0:
            if self._raise_errors_on_empty_op:
                raise QueueIsEmptyError("Cannot peek from an empty queue")
            return None
        return self._items[0]

    def size(self) -> int:
        """Returns the size of the queue."""
        return len(self._items)
    
    def is_empty(self) -> bool:
        """Returns `True` if the queue is empty, otherwise `False`."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Returns `True` if `max_size` is set and the queue is full, otherwise `False`."""
        return self._max_size != None and self.size() >= self._max_size