from collections.abc import Callable, Iterable
from typing import Any
from numbers import Number


def insertion_sort(iterable: Iterable, key: Callable[[Any], Number] = None, reverse: bool = False) -> list:
    """
    Sorts a copy of the iterable in place and retuns it as a list.

    Pros: fast (for small lists), adaptive, stable.
    
    Parameters
    ----------
    - iterable : Iterable
        Iterable that needs to be sorted.
    - key : func, optional
        Function that returns key used for sorting.
        (default = None)
    - reverse : bool, optional
        Set to True to sort from biggest to lowest.
        (default = False)

    Returns
    -------
    - list
        Sorted *copy* of the iterable.
    """

    iterable = list(iterable)

    for i in range(1, len(iterable)):
        j = i
        while j>0:
            left_val = iterable[j-1] if key == None else key(iterable[j-1])
            right_val = iterable[j] if key == None else key(iterable[j])

            if (not reverse and left_val <= right_val) or (reverse and left_val >= right_val):
                break
            iterable[j-1], iterable[j] = iterable[j], iterable[j-1]
            j -= 1
    
    return iterable
