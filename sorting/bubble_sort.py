from collections.abc import Callable, Iterable
from typing import Any
from numbers import Number


def bubble_sort(iterable: Iterable, key: Callable[[Any], Number] = None, reverse: bool = False) -> list:
    """
    Baby's first sort.
    Here just to party.

    Sorts a copy of the iterable in place and returns as a list.

    Cons: has no pros.

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
    swapping = True
    end = len(iterable)

    while swapping:
        swapping = False

        for i in range(1, end):
            left_val = iterable[i-1] if key == None else key(iterable[i-1])
            right_val = iterable[i] if key == None else key(iterable[i])

            if (not reverse and left_val > right_val) or (reverse and left_val < right_val):
                iterable[i-1], iterable[i] = iterable[i], iterable[i-1]
                swapping = True

        end -= 1

    return iterable
