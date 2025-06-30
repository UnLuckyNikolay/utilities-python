from collections.abc import Callable, Iterable
from typing import Any
from numbers import Number

def selection_sort(iterable: Iterable, key: Callable[[Any], Number] = None, reverse: bool = False) -> list:
    """
    Sorts a copy of the iterable in place and retuns it as a list.

    Pros: in-place, n amount of swaps.
    Cons: slow, unstable.
    
    Parameters
    ----------
    iterable : Iterable
        Iterable that needs to be sorted
    key : func, optional
        Function that returns key used for sorting
    reverse : bool, optional
        Set to True to sort from biggest to lowest

    Returns
    -------
    list
        Sorted *copy* of the iterable
    """

    iterable = list(iterable)

    for i in range(0, len(iterable)):
        next_i = i
        for j in range(i+1, len(iterable)):
            next_val = key(iterable[next_i]) if key != None else iterable[next_i]
            current_val = key(iterable[j]) if key != None else iterable[j]

            if (not reverse and current_val < next_val) or (reverse and current_val > next_val):
                next_i = j
        
        iterable[i], iterable[next_i] = iterable[next_i], iterable[i]

    return iterable