#!/usr/bin/env python3
"""
2-measure_runtime.py

This module contains a coroutine `measure_runtime` that measures the runtime
of executing `async_comprehension` four times in parallel.
"""

import asyncio
import time
import importlib

# Dynamically import the module to handle unconventional naming
async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime of running async_comprehension four times in parallel

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
