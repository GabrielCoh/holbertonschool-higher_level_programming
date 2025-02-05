#!/usr/bin/python3
"""
Module that writes a class Square that inherits through Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that represents a square and is inheriting through BaseGeometry
    """

    def __init__(self, size):
        """
        Initialization of a Square instance

        Args:
            size(int): the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculation of the area"""
        return (self.__size * self.__size)

    def __str__(self):
        """Return a string representing the square"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
