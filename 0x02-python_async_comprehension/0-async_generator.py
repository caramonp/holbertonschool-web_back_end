#!/usr/bin/env python3
"""[coroutine called async_generator]
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times, each time asynchronously wait 1 second

    Yields:
        Generator[float, None, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
