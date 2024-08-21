#!/usr/bin/env python3
"""
1-async_comprehension.py

This module contains a coroutine `async_comprehension` that collects 10 random
numbers from the `0-async_generator` coroutine using an async comprehension.
"""

from typing import List
import asyncio
import importlib

# Dynamically import the module to handle unconventional naming
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from `async_generator` using an
    async comprehension and returns them as a list.

    Returns:
        List[float]: A list of 10 random float numbers collected from
        `async_generator`.
    """
    return [num async for num in async_generator()]
