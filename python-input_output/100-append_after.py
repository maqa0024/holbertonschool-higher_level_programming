#!/usr/bin/python3
"""Module that provides a function to insert a line after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename (str): Path to the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line to insert after each matching line.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in content:
            f.write(line)
            if search_string in line:
                f.write(new_string)
