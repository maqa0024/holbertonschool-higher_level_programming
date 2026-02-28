#!/usr/bin/python3
"""Module that defines the MyList class, inheriting from list."""


class MyList(list):
    """A custom list class that extends the built-in list.

    Inherits all list behavior and adds a method to print sorted output
    without modifying the original list.
    """

    def print_sorted(self):
        """Print the list elements sorted in ascending order.

        The original list remains unchanged.
        """
        print(sorted(self))
