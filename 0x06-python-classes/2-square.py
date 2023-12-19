#!/usr/bin/python3
"""Square module - contains a Square class to manage size attributes
and perform type and value checks."""


class Square:
    """Defines a square with a private instance attribute: size"""

    def __init__(self, size=0):
        """
        Initializes a new Square .

        Args:
            size (int):  Length of a side of the square..
                Raises:
                    TypeError: If the size is not an integer.
                    ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
