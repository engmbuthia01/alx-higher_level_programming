#!/usr/bin/python3
"""
This module defines a function that
appends text at the end of a file
"""


def append_write(filename="", text=""):
    """append text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
