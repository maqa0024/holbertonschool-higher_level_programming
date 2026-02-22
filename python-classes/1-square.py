#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Defines a square with a private instance attribute: size."""

    def __init__(self, size):
        """Initializes a new Square.
        Args:
            size: The size of the square (no validation yet).
        """
        self.__size = size
