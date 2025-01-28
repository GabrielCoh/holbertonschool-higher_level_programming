#!/usr/bin/python3
"""
This module defines a class Square by it's private instance attribute: size
"""


class Square:
    """
    A class that defines a square with a private size attribute

    Attribute:
        __size (int): Size of the square
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class

        Args:
            size (int): Size of the square
        """
        self.__size = size
