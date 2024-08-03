#!/usr/bin/env python3
"""This is a module that creates a type-annotated function add that takes
a float a and a float b as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """This method returns their sum as a float
    Args:
    a (float): the first float number
    b (float): the second float number

    Returns:
    float: sum of numbers"""
    return a + b
