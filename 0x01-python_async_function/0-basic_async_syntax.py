#!/usr/bin/env python3
''' python async'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Generate a random floating-point number between 0 and max_delay (inclusive)'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
