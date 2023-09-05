#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    def __init__(self, width=0, h=0):
        self.width = width
        self.h = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        if type(value) is not int:
            raise TypeError("h must be an integer")
        if value < 0:
            raise ValueError("h must be >= 0")

        self.__h = value

    """Instance methods that return the area
        and perimeter of a rectangle"""
    def area(self):
        return self.width * self.h

    def perimeter(self):
        if self.width == 0 or self.h == 0:
            return 0
        return 2 * (self.width + self.h)

    """Prints out a rectangle in string form"""
    def __str__(self):
        rect = ""

        if self.width == 0 or self.h == 0:
            return rect
        for i in range(self.h):
            for j in range(self.width):
                rect += '#'

            if i != self.h - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        return f"Rectangle({self.width}, {self.h})"
