#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer argument """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of all delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delay_task = [await task for task in asyncio.as_completed(tasks)]
    return delay_task
  