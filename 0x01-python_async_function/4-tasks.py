#!/usr/bin/env python3
"""
4-tasks.py

Module contains a function `task_wait_n` that spawns multiple task_wait_random
tasks concurrently and returns a list of the delays in ascending order.
"""

import asyncio
from typing import List
import importlib

# Dynamically import task_wait_random from the 3-tasks module
task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns multiple `task_wait_random` tasks concurrently.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for `task_wait_random`.

    Returns:
        List[float]: A list of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
