#!/usr/bin/python3
"""
Defines a class Square
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes the square with a private instance: size

        Args:
            size (int): Size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area

        Return:
            int: Area of the square
        """
        return self.__size ** 2
