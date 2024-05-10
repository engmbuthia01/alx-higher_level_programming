#!/usr/bin/python3
"""
This module defines a class square that
inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """Inherits from the rectangle"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size
