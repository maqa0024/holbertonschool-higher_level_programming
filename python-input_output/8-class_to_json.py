#!/usr/bin/python3
"""Module that provides a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
