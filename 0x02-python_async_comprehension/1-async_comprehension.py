#!/usr/bin/env python3
"""[coroutine called async_generator]
"""
import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float]:
    """[oroutine will collect 10 random numbers using an async comprehensing]

    Returns:
        [float]: [10 radom numbers from async_genrator]

    """
    return [i async for i in async_generator()]
