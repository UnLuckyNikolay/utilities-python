from collections.abc import Callable, Iterable
from typing import Any
from numbers import Number
from shuffle import shuffle

def quick_sort(iterable: Iterable, key: Callable[[Any], Number] = None, reverse: bool = False, shuffling: bool = True) -> list:
    """
    Sorts a shuffled (can be turned off) copy of the iterable in place and retuns it as a list.

    Pros: fast, in-place.
    Cons: Slow if iterable is pre-sorted (shuffles it by default), unstable, recursive.
    
    Parameters
    ----------
    iterable : Iterable
        Iterable that needs to be sorted.
    key : func, optional
        None by default. Function that returns key used for sorting.
    reverse : bool, optional
        False by default. Set to True to sort from biggest to lowest.
    shuffling : bool, optional
        True by default. Shuffles the iterable to make sure it isn't pre-sorted.

    Returns
    -------
    list
        Sorted *copy* of the iterable.
    """

    iterable = shuffle(iterable) if shuffling else list(iterable)
    low = 0
    high = len(iterable) - 1

    _inner_recursion(iterable, low, high, key, reverse)

    return iterable
    
def _inner_recursion(iterable: Iterable, low: int, high: int, key: Callable[[Any], Number], reverse: bool):
    """
    Inner recursive function for quick_sort. 
    
    Calls _inner_sort, gets a pivot, then calls itself twice to the left and around parts around the pivot.
    """

    if low < high:
        pivot = _inner_sort(iterable, low, high, key, reverse)
        _inner_recursion(iterable, low, pivot-1, key, reverse)
        _inner_recursion(iterable, pivot+1, high, key, reverse)


def _inner_sort(iterable: Iterable, low: int, high: int, key: Callable[[Any], Number], reverse: bool) -> int:
    """
    Inner function for quick_sort. 
    
    Chooses the last object in the chosen part of the list as pivot and sorts around it.
    """
    
    pivot = iterable[high] if key==None else key(iterable[high])
    i = low - 1
    for j in range(low, high):
        if (    
                (key!=None and 
                ((not reverse and key(iterable[j]) < pivot) or (reverse and key(iterable[j]) > pivot)))
            or 
                (key==None and 
                ((not reverse and iterable[j] < pivot) or (reverse and iterable[j] > pivot))) 
        ):
            i+=1
            iterable[i], iterable[j] = iterable[j], iterable[i]
        
    i+=1
    iterable[i], iterable[high] = iterable[high], iterable[i]
    return i