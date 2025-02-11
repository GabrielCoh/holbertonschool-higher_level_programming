#!/usr/bin/python3
"""Function that reads a text file and prints it to the output"""


def read_file(filename=""):
    """
    Read a text file

    Args:
        filename(str): the text file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
