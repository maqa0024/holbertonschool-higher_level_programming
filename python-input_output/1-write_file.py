#!/usr/bin/python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return characters written.

    Args:
        filename (str): Path to the file to write.
        text (str): The string content to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
