#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer argument """
import asyncio
import time

wait_n =  __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int)-> List[float]:
    """returns total_time / ni measure"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
