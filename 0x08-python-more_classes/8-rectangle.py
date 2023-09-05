#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, w=0, height=0):
        Rectangle.number_of_instances += 1
        self.w = w
        self.height = height

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
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """Instance methods that return the area
        and perimeter of a rectangle"""
    def area(self):
        return self.w * self.height

    def perimeter(self):
        if self.w == 0 or self.height == 0:
            return 0
        return 2 * (self.w + self.height)

    """Returns a rectangle in string form"""
    def __str__(self):
        rect = ""

        if self.w == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            for j in range(self.w):
                rect += str(self.print_symbol)

            if i != self.height - 1:
                rect += '\n'
        return rect

    """Returns a string representation of the instance creation"""
    def __repr__(self):
        return f"Rectangle({self.w}, {self.height})"

    """Runs when an instance is deleted"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """Returns the Rectangle instance with a bigger area"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
