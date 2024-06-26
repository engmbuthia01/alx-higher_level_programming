#!/usr/bin/python3
"""
This module defines a function
that reads a teext file and prints it to standard output
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
