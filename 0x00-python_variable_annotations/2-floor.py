#!/usr/bin/env python3
"""This is a module that creates a type-annotated function floor which
takes a float n as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """This method returns the floor of the float.
    Args:
    n (float): the first float

    Returns:
    int: returns the floor of the float."""
    return math.floor(n)
