#!/usr/bin/python3
"""
defines a class that prevents the user from dynamically
creating new instance attributes except if the
new instance attribute is called first_name
"""


class LockedClass:
    """prevents a user from creating a new instance"""
    __slots__ = ["first_name"]
