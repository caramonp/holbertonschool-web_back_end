#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer argument """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of delayed async tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    daly_task = [await task for task in asyncio.as_completed(tasks)]
    return daly_task