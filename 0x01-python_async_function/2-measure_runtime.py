import time
import asyncio
from concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
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

    return total_time / n