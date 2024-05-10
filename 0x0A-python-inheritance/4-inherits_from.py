#!/usr/bin/python3
"""
This module containts a function that checks
if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class 
    Args:
        obj: The object
        a_class: The class
    Return:
        Booloean (True or False
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
