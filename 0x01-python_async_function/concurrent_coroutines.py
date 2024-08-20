#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

This module contains an async routine `wait_n` that spawns `wait_random`
n times with the specified max_delay and returns the list of all the delays
in ascending order.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.

    Returns:
        List[float]: A list of all delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
