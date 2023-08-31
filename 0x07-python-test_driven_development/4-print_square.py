#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square  module supplies one function, print_square(square_size).
"""

def print_square(square_size):
    """prints a square with "#"'s that has a length of square_size """
    if type(square_size) is not int:
        raise TypeError("square_size must be an integer")
    if square_size < 0:
        raise ValueError("square_size must be >= 0")
    if square_size > 0:
        print(("#" * square_size + "\n") * square_size, end="")
