#!/usr/bin/python3
"""
This module defines a class Student
with defined public instance attributes
"""


class Student:
    """ Student class body."""

    def __init__(self, first_name, last_name, age):
        """Initialize student props in contructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
