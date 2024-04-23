#!/usr/bin/python3
"""Header"""

import json


class Base:
    """
    This is the Base class,
    which will serve as the base class for other classes in the project.

    Attributes:
    - __nb_objects (int): Private class attribute to manage the id attribute.
    - id (int): Public instance attribute to store the object's id.

    Methods:
    - __init__(self, id=None): Constructor method to initialize the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance.

        Args:
        - id (int, optional): Object's id.
        If provided, assign it to the id attribute;
          otherwise, increment __nb_objects
          and assign the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
        - list_dictionaries (list): List of dictionaries.

        Returns:
        - str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
