#!/usr/bin/python3

"""
My addition module
"""


def add_integer(a, b=98):
    """This function adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer, default value set to 98.

    Returns:
        int: The sum of two integers.

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
