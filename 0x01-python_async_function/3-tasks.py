#!/usr/bin/env python3
"""
3-tasks.py

This module contains a function `task_wait_random` that returns an asyncio.Task
object for the `wait_random` coroutine.
"""

import asyncio
import importlib

# Dynamically import wait_random from the 0-basic_async_syntax module
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The asyncio.Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
