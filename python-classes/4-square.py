#!/usr/bin/python3
"""
This module is used to create a class square that defines a square
"""


class Square:
    """
    Defines a square with private instance attribute: size

    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Property:
        to retrieve it = def size(self)
        so set it = def size(self, value)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Defines the area of the square

    Return:
        The current square area
    """
    def area(self):
        return self.__size ** 2
