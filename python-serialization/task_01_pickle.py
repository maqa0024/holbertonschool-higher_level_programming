#!/usr/bin/env python3
"""Module for custom object serialization using pickle."""
import pickle


class CustomObject:
    """A custom class demonstrating pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject.

        Args:
            name (str): The object's name.
            age (int): The object's age.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The output file path.

        Returns:
            None on failure.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject instance from a file.

        Args:
            filename (str): The input file path.

        Returns:
            CustomObject instance, or None if file is missing or malformed.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
