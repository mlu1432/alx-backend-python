#!/usr/bin/env python3
"""
2-measure_runtime.py

This module contains a function `measure_time` that measures the total
execution time for the `wait_n` coroutine and returns the average time per coroutine.
"""

import time
import asyncio
import importlib

# Dynamically import wait_n from the 1-concurrent_coroutines module
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time function measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    # Debugging output
    print(f"Start time: {start_time}")
    print(f"End time: {time.time()}")
    print(f"Total time: {total_time}")

    # Return the average time per coroutine
    return total_time / n
