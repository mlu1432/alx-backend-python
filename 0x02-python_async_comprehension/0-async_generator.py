#!/usr/bin/env python3
"""
0-async_generator.py

This module contains a coroutine `async_generator` that yields a random
number between 0 and 10 asynchronously, 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates a sequence of 10 random numbers between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
