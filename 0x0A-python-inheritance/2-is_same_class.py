#!/usr/bin/python3
"""
This module checkes whether
an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class ;
    otherwise False
    """

    if type(obj) == a_class:
        return True
    else:
        False
