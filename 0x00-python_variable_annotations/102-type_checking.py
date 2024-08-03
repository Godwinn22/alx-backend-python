#!/usr/bin/env python3
"""Task 102 module.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This method creates multiple copies of items in a tuple.

    Args:
    lst (Tuple): The tuple to be copied.
    factor (int): The number of times to copy the tuple.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
