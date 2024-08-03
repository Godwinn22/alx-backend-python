#!/usr/bin/env python3
"""This is a module that creates a type-annotated function concat
that takes a string str1 and a string str2 as arguments and
returns a concatenated string

Keyword arguments:
str1 -- str
str2 -- str
Return: returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """This method returns a concatenated string
    Args:
    str1 (str): the first string
    str2 (str): the second string

    Returns:
    str: returns a concatenated string"""
    return str1 + str2
