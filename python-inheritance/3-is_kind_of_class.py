#!/usr/bin/python3
"""Module that defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or any class inheriting from it.
    """
    return isinstance(obj, a_class)
