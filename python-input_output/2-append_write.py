#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file
    and return teh numbers of characters added

    Args:
        filename(str): The name of the file
        text(str): The text to append

    Return:
        The number of characters added to the string
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
