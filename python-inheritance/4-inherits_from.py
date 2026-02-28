#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object must be an instance of a class that inherited (directly or
    indirectly) from a_class, but NOT an instance of a_class itself.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        True if obj's class is a subclass (not exact) of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
