#!/usr/bin/python3
"""
Module that returns True if the object is an instance of a class
that inherited (directly or indirectly) the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Prints if the object is an instance that inherited through the specified class

    Args:
        obj: the object to compare
        a_class: the class to compare it to

    Return:
        True if the object inherited through a_class, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
