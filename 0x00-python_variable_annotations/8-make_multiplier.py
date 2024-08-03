#!/usr/bin/env python3
"""This is a module that creates a type-annotated function make_multiplier that
takes a float multiplier as argument and returns a function that multiplies
a float by multiplier.

Keyword arguments:
multiplier -- float
Return: returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This method returns a function that multiplies a float by multiplier..
    Args:
    multiplier (float): a float numbers

    Returns:
    float: returns a function that multiplies a float by multiplier.."""
    return lambda x: x * multiplier
