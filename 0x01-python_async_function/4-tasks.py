#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int):
    """
    Task wait n
    """
    return wait_n(n, max_delay)
