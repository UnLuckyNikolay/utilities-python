from collections.abc import Callable, Iterable
from typing import Any
from numbers import Number


def merge_sort(iterable: Iterable, key: Callable[[Any], Number] = None, reverse: bool = False) -> list:
    """
    Sorts the iterable by splitting into smaller and smaller iterables before merging back. Then returns it as a list.

    Pros: fast and stable.
    Cons: requires more memory, recursive.

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

    if len(iterable) < 2:
        return iterable
    
    middle = len(iterable) // 2
    left, right = iterable[:middle], iterable[middle:]

    return _merge(merge_sort(left, key, reverse), merge_sort(right, key, reverse), key, reverse)

def _merge(left: Iterable, right: Iterable, key: Callable[[Any], Number], reverse: bool) -> list:
    """
    Inner function for merge_sort used to merge split lists back.

    Parameters
    ----------
    left : Iterable
        Left half of the iterable
    right : Iterable
        Right halt of the iterable
    key : func
        Function that returns key used for sorting
    reverse : bool
        Set to True to sort from biggest to lowest

    Returns
    -------
    list
        Sorted *copy* of the iterable
    """

    final = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        left_val = left[i] if key == None else key(left[i])
        right_val = right[j] if key == None else key(right[j])
        if (not reverse and left_val <= right_val) or (reverse and (left_val >= right_val)):
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    if i < len(left):
        final.extend(left[i:])
    if j < len(right):
        final.extend(right[j:])

    return final
