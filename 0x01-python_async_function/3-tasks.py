#!/usr/bin/env python3
"""
2. Measure runtime
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Task wait random
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
