#!/usr/bin/python3
"""
Module that writes a class Rectangle that is based on BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Prints a rectangle wkth the area of said rectangle"""
    def __init__(self, width, height):
        """
        Args:
        width: private instance positive int validated by integer_validator
        height: private instance positive int validated by integer_validator

        Return:
            area of the rectangle
            __str__ function to divide width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return(f"[Rectangle] {self.__width}/{self.__height}")
