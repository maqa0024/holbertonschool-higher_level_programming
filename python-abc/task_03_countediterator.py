#!/usr/bin/python3
"""Module that defines the CountedIterator class."""


class CountedIterator:
    """An iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize CountedIterator with an iterable.

        Args:
            iterable: Any iterable object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself."""
        return self
