#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is a string and the second element is the square of a number.

    Args:
        k (str): The string value.
        v (Union[int, float]): The integer or float to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string and the second element is the squared value of v.
    """
    return (k, float(v ** 2))
