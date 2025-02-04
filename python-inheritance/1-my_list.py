#!/usr/bin/python3
"""
Module that inherits from a list
"""


def MyList(list):
    """
    Prints a class from a sorted list

    Raise:
        TypeError: element must be an integer

    Test:
        test file is 1-my_list.txt in the tests directory
    """
    def sum(self):
        if not all(isinstance(e, int) for e in self):
            raise TypeError("element must be an integer")
        return sum(i * e for i, e in enumerate(self))

    def print_sorted(self):
        if not all(isinstance(e, int) for e in self):
            raise TypeError("element must be an integer")
        print(sorted(self))
