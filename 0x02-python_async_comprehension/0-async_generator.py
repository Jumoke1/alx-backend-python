#!/usr/bin/env python3
'''Python - Async Comprehension'''
import asyncio
import random
from typing import Generaator


async def async_generator() -> Generator[float, None, None]:
    ''' a coroutine that will loop 10 times and wait 1sec'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
