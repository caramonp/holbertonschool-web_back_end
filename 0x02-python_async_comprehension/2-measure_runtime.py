#!/usr/bin/env python3
"""[coroutine called async_generator]
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
  """Run time for four parallel comprehensions

  Returns:
      float: [runtime]
  """
    start = time.time()
    await asyncio.gather(
      async_comprehension()
    )
    end = time.time()
    return end-start
