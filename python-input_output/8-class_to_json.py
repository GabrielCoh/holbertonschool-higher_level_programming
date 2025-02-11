#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Function that returns the dictionnary description with simple
    date structure for JSON serialization of an object

    Args:
        obj: An instance od a Class

    Return:
        Dictionnary simple date structure (int, str, etc)
    """
    return obj.__dict__
