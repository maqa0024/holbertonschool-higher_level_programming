#!/usr/bin/python3
"""Module that provides a function to read and print a text file to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout.

    Args:
        filename (str): Path to the file to be read. Defaults to empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
