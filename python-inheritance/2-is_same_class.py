#!/usr/bin/python3
"""
Module that returns True if the object is an instance
of the exact specified class
"""


def is_same_class(obj, a_class):
    """
    Prints the object which si an instance of the specfied class
    """
    return type(obj) is a_class
