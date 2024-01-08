#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list object with available attributes and methods of an object.

    Parameters:
        obj: The object to look up.

    Returns:
        A list containing attributes and methods of the object.
    """
    return dir(obj)
