#!/usr/bin/env python3
"""This is a module that annotate the below function's parameters
and return valueswith the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This method annotates a function's parameters and return
    values with the appropriate types

    Args:
    lst (any type): a parameter of any type

    Returns:
    float:  return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
