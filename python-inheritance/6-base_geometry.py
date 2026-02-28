#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """Raise an Exception - subclasses must implement area()."""
        raise Exception("area() is not implemented")
