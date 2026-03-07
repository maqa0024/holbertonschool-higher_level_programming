#!/usr/bin/python3
"""Module that defines a Student class with serialization & deserialization."""


class Student:
    """A class that defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: The dictionary with all or filtered attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names
            and values are the corresponding attribute values.
        """
        for k, v in json.items():
            setattr(self, k, v)
