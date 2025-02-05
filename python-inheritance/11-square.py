#!/usr/bin/python3
"""Module that writes a Square that inherits through Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square and inherited from BaseGeometry"""
    def __init__(self, size):
        """
        Initialization of a square instance

        Args:
            size(int): The square's size

        Raise:
            Exception
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculation of the area"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representing the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
