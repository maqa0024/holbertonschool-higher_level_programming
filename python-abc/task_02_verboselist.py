#!/usr/bin/python3
"""Module that defines the VerboseList class."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Add item to the list and print a notification.

        Args:
            item: The item to add.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and print a notification.

        Args:
            items: The iterable of items to add.
        """
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove item from the list and print a notification.

        Args:
            item: The item to remove.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from the list and print a notification.

        Args:
            index (int): The index to pop. Defaults to -1 (last item).
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
