#!/usr/bin/env python3
"""
This module provides a function that creates a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the specified multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    
    return multiplier_function
