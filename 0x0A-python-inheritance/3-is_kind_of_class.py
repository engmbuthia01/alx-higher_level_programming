#!/usr/bin/python3
"""
This module checks whether a given object is
an instance of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks whether a given object is an
    instance of a class or an inherited class
    Args:
        obj (any): object
        a_class (type): the class
    Returns:
        Boolean (True & False)
    """

    return (isinstance(obj, a_class))
