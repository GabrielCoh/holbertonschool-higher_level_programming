#!/usr/bin/python3
"""
Module that returns True if the object is an instance,
or if the object is an instance of a class that inherited
the specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    if type(obj) is a_class:
        return True
    elif isinstance(obj, a_class):
        return True
    else:
        return False
