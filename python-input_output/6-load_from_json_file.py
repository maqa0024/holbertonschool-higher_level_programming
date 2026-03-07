#!/usr/bin/python3
"""Module that provides a function to create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
