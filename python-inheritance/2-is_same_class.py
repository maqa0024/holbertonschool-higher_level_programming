#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, False otherwise.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        True if type(obj) is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
