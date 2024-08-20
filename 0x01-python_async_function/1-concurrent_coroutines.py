#!/usr/bin/env python3
import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times and returns a list in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )
    return sorted(delays)