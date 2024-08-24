#!/usr/bin/env python3
"""
0-basic_async_syntax.py

This module contains a coroutine `wait_random` that waits for a random
delay between 0 and max_delay seconds and returns the delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns
    the actual delay.

    Args:
        max_delay (int): The maximum delay time in seconds (inclusive).

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
