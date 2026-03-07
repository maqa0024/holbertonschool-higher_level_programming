#!/usr/bin/python3
"""Module that provides a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize and write.
        filename (str): Path to the file to write the JSON data to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
