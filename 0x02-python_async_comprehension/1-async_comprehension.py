#!/usr/bin/env python3
"""Asynchronous Comprehension"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    The coroutine will collect 10 random numbers using an async comprehensing
    """
    result = [i async for i in async_generator()]
    return result
