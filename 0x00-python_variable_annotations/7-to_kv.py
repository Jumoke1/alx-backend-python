#!/usr/bin/env python3
'''
 function to_kv that takes a string k and an int OR float v as
 arguments and returns a tuple.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns a tuple where the first element is the string k and the second
    element is the square of v.

    Args:
        k (str): The string element.
        v (Union[int, float]): The integer or float element to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the
        square of v as a float.
    '''
    return(k, float(v**2))
