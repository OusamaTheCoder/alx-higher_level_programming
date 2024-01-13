#!/usr/bin/python3
"""
Module for defining the Student class.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list,
            of strings representing attribute names to retrieve.

        Returns:
            dict: A dictionary,
            with the specified attributes of the Student instance.
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {attr:
                    getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
