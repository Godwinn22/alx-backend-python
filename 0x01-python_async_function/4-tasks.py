#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Task wait n
    """
    tasks = []
    for _ in range(n):
        ye = task_wait_random(max_delay)
        tasks.append(ye)
    coroutine = await asyncio.gather(*tasks)
    return sorted(coroutine)
