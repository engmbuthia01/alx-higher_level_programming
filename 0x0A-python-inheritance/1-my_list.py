#!/usr/bin/python3
"""Mylist inhertits the list class"""

class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
