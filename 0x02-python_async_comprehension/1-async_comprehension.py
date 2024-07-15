#!/usr/bin/env python3
'''Async Comprehensions'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[int]:
    '''A coroutine called async_comprehension that takes
    no arguments and returns a list of 10 random integers.
    '''
    return [num async for num in async_generator()]
