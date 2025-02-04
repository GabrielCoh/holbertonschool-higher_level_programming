#!/usr/bin/python3
"""
Module that writes a class Rectangle that is based on BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Args:
        width: private instance positive int validated by integer_validator
        height: private instance positive int validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
