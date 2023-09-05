#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """The Rectangle class"""
    def __init__(self, w=0, h=0):
        self.h = h
        self.w = w

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
