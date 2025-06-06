#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """
    Defines a rectangle with optional width and height

    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__heght == 0:
            return ("")
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += "#" * self.__width
                if i < self.__height - 1:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
