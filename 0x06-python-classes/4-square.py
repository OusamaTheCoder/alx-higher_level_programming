#!/usr/bin/python3
"""Square module - manages the size attribute of a square
and ensures type and value validation"""


class Square:
    """Represents a square with a private instance attribute size"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of the side of a square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size.

        Args:
            value: The size value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
