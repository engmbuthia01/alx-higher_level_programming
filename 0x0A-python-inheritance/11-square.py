#!/usr/bin/python3
"""
This module defines a class Square that
inherits from Rectangle (9-rectangle.py)
"""


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
