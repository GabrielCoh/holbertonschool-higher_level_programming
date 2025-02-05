#!/usr/bin/python3
"""
Module that writes a class BaseGeometry
"""


class BaseGeometry:
    """A BaseGeometry class"""


    def area(self):
        """This is an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name (str): name of the parameter
            value (int): the parameter

        Raise:
            TypeError: 'name' must be an integer
            ValueError: 'name' must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
