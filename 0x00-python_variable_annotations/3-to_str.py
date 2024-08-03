#!/usr/bin/env python3
"""This is a module that creates a type-annotated function to_str that
takes a float n as argument and returns the string representation of the float.

Keyword arguments:
n -- float
Return: returns the string representation of the float.
"""
import math


def to_str(n: float) -> str:
    """This method returns the string representation of the float..
    Args:
    n (float): the first float

    Returns:
    str: returns the string representation of the float.."""
    return str(n)
