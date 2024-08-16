#!/usr/bin/env python3
"""
This module provides a function to sum a list of float numbers.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result as a float.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
