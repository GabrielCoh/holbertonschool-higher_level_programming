#!/usr/bin/python3
"""
Creates a class square that defnes a square
"""


class Square:
    """
    Defines a square with private instance attribute: size

    Args:
        size (int): size of the square

    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
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
            raise ValueError("size must >= 0")
        self.__size = value

    """
    Defines a public area of a square

    Return:
        The current square area
    """
    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
