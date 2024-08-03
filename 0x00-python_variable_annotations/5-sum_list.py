#!/usr/bin/env python3
"""This is a module that creates a type-annotated function sum_list which takes
a list input_list of floats as argument and returns their sum as a float.

Keyword arguments:
input_list -- list
Return: returns the sum of all float numbers in a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This method returns the sum of all float numbers in a list.
    Args:
    input_list (list): a list of float numbers

    Returns:
    float: returns the sum of all float numbers in a list."""
    sum: float = 0
    for val in input_list:
        sum += val
    return sum
