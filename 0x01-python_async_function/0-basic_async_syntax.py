##!/usr/bin/env python3
'''python async.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    delays = random.random() * max_delay
    await asyncio.sleep(delays)
    return delays
