from collections.abc import Iterable
from random import randint


def shuffle(iterable: Iterable) -> list:
    """
    Shuffles a copy of the iterable in place and returns it as a list.

    Uses Fisher-Yates shuffle (complexity - O(n)).

    Parameters
    ----------
    - iterable : Iterable
        Iterable to be shuffled.
    
    Returns
    -------
    - list
        A shuffled *copy* of the iterable.
    """

    iterable = list(iterable)
    i = len(iterable)

    while i > 1:
        i -= 1
        rnd = randint(0, i)
        iterable[i], iterable[rnd] = iterable[rnd], iterable[i]

    return iterable