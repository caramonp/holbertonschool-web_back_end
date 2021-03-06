#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer argument """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of delayed async tasks"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return delayed_tasks
