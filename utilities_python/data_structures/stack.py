from typing import Any


class StackIsEmptyError(Exception):
    """Custom exception raised when pop or peek operation is performed on an empty stack."""
    pass

class StackIsFullError(Exception):
    """Custom exception raised when push operation is performed on a full stack."""
    pass

class Stack:
    """
    Abstract data structure. Last in, first out.
    Complexity of all methods - O(1).

    Methods
    -------
    - push(item)
        Puts an item at the top of the stack.

    - pop -> Any | None
        Removes and returns the item on top of the stack.
        Returns `None`/raises `StackIsEmptyError` if stack is empty, depending on `raise_errors_on_empty_op`.

    - peek -> Any | None
        Returns the item on top without removing it.
        Returns `None`/raises `StackIsEmptyError` if stack is empty, depending on `raise_errors_on_empty_op`.

    - size -> int
        Returns the size of the stack.

    - is_empty -> bool
        Returns `True` if stack is empty, otherwise `False`.

    - is_full -> bool
        Returns `True` if `max_size` is set and the stack is full, otherwise `False`.

    Raises
    ------
    - StackIsFullError
        If `max_size` is set and `push` is performed when size of the stack equals `max_size`.

    - StackIsEmptyError
        If `raise_errors_on_empty_op` is set to `True` and `peek`/`pop` is performed on an empty stack.
    """
    
    def __init__(self, max_size: int = None, raise_errors_on_empty_op: bool = False): # pyright: ignore[reportArgumentType]
        """
        Args
        ----
        - max_size : int, optional
            Maximum size of the stack. 
            (default = None)

        - raise_errors_on_empty_op : bool, optional
            Changes `peek`/`pop` to raise errors if the stack is empty instead of returning `None`.
            (default = False)
        """
        self._items = []
        self._max_size = max_size
        self._raise_errors_on_empty_op = raise_errors_on_empty_op

    def __repr__(self):
        items_repr = ", ".join(repr(item) for item in reversed(self._items))
        return f"Stack[{items_repr}]"

    def __iter__(self):
        return reversed(self._items)
    
    def __eq__(self, other):
        if not isinstance(other, Stack):
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
        Puts an item at the top of the stack.
        
        Raises `StackIsFullError` if `max_size` is set and size of the stack equals `max_size`.
        """
        if self._max_size != None and self.size() >= self._max_size:
            raise StackIsFullError("Cannot push to a full stack.")
        self._items.append(item)

    def pop(self) -> Any | None:
        """
        Removes and returns the item on top of the stack.
        
        Returns `None`/raises `StackIsEmptyError` if stack is empty, depending on `raise_errors_on_empty_op`.
        """
        if len(self._items)==0:
            if self._raise_errors_on_empty_op:
                raise StackIsEmptyError("Cannot pop from an empty stack.")
            return None
        item = self._items.pop(-1)
        return item

    def peek(self) -> Any | None:
        """
        Returns the item on top without removing it.

        Returns `None`/raises `StackIsEmptyError` if stack is empty, depending on `raise_errors_on_empty_op`.
        """
        if len(self._items)==0:
            if self._raise_errors_on_empty_op:
                raise StackIsEmptyError("Cannot peek from an empty stack")
            return None
        return self._items[-1]

    def size(self) -> int:
        """Returns the size of the stack."""
        return len(self._items)
    
    def is_empty(self) -> bool:
        """Returns `True` if the stack is empty, otherwise `False`."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Returns `True` if `max_size` is set and the stack is full, otherwise `False`."""
        return self._max_size != None and self.size() >= self._max_size