#!/usr/bin/env python3
"""This is a module that creates a type-annotated function sum_list which takes
a list mixed lst of floats as argument and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This method returns the sum of all float numbers in a list.
    Args:
    mxd_lst (list): a list of float numbers

    Returns:
    float: returns the sum of all float numbers in a list."""
    sum: float = 0
    for val in mxd_lst:
        sum += val
    return sum
