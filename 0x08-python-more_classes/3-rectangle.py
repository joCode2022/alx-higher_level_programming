#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, value):
        if type(value) is not int:
            raise TypeError("w must be an integer")
        if value < 0:
            raise ValueError("w must be >= 0")

        self.__w = value

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
        return self.w * self.h

    def perimeter(self):
        if self.w == 0 or self.h == 0:
            return 0
        return 2 * (self.w + self.h)

    """Prints out a rectangle in string form"""
    def __str__(self):
        rect = ""

        if self.w == 0 or self.h == 0:
            return rect
        for i in range(self.h):
            for j in range(self.w):
                rect += '#'

            if i != self.h - 1:
                rect += '\n'
        return rect
