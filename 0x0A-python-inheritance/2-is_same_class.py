#!/usr/bin/python3
"""
This module checkes whether
an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks whether an object is exactly an instance of the specified class
    Args:
        obj: object
        a_class: the class
    Return: True or False
    """
    
    return (type(obj) == a_class)
