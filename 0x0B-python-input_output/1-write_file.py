#!/usr/bin/python3
"""
This module defines a function
that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string, returns number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
