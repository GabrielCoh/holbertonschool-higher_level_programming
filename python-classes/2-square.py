#!/usr/bin/python3
"""
Class Square that defines a class Square
"""


class Square:
    """
    Class that defines a square by its size
    With exceptions

    Attributes:
    __size (int): Size of the square
    """

    def __init__(self, size=0):
        """
        Initializes the square with a private instance attribute: size

        Args:
            size (int): Size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
