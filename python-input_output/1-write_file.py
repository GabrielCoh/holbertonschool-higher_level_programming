#!/usr/bin/python3
"""Function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Writes a string to a text files and returns its number of characters

    Args:
        filename(str): The name of the file
        text(str): The text to write into the text file

    Return:
        The number of characters written in the string
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
