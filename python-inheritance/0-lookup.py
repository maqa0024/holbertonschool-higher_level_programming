#!/usr/bin/python3
"""Module that provides a lookup function for object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
