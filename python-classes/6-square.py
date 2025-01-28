#!/usr/bin/python3
"""
Creates a class square that defines a  square
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Defines a square with private size and private position

        Args:
            size (int): The size of the square

        Raise:
            TypeError: if size is not an integer
            ValueError: if size >= 0
            TypeError: if position is not a tuple of two integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Defines the size of the square

        Args:
            value (int): The size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: is size >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Defines the position of the square

        Args:
            value (tuple): The position fo the square

        Raises:
            TypeError: if position is not a tuple of two positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the current square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with #

        If size is equal an empty line will be printed
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
