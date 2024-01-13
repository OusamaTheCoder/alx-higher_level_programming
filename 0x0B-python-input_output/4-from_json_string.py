#!/usr/bin/python3
"""
Module for converting a JSON string to an object (Python data structure).
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
