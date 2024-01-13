#!/usr/bin/python3
"""
Module for converting an object of a Class to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple,
    data structure for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary with serializable attributes.
    """
    return obj.__dict__
