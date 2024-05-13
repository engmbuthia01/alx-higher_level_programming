#!/usr/bin/python3
"""
This is a module that defines a
base class
"""


class Base:
    """This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor initializing
        objects of a class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
