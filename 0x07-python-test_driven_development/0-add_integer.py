#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def add_integer(c, d):
    """Return the addition of two numbers."""
    if type(c) is not int and type(c) is not float:
        raise TypeError("a must be an integer")
    if type(d) is not int and type(d) is not float:
        raise TypeError("b must be an integer")
    if type(c) is float:
        a = int(c)
    if type(d) is float:
        d = int(d)
    return c + d
