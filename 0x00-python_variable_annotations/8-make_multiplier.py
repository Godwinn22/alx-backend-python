#!/usr/bin/env python3
"""This is a module that annotate the below function's parameters
and return valueswith the appropriate types.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This method returns a function that multiplies a float by multiplier..
    Args:
    multiplier (float): a float numbers

    Returns:
    float: returns a function that multiplies a float by multiplier.."""
    return lambda x: x * multiplier
