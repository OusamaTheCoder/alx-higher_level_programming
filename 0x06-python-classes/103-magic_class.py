#!/usr/bin/python3
"""
Magic class - Implements geometric calculations using Python bytecode
"""

import math


class MagicClass:
    """
    Code derived from Python bytecode.
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a specified radius.

        Args:
            radius: The radius of the circle.

        Raises:
            TypeError: If radius is neither an int nor a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
