#!/usr/bin/env python3
"""Asynchronous Generator"""

import asyncio
import random


async def async_generator() -> float:
    """Write a coroutine called async_generator that takes no arguments."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
