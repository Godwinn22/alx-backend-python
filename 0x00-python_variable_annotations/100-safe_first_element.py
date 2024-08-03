#!/usr/bin/env python3
"""
Task 100 module
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This method annotates a function's parameters and return
    values with the appropriate types

    Args:
    lst (any type): a parameter of any type

    Returns:
    float:  return values with the appropriate types"""
    if lst:
        return lst[0]
    else:
        return None
