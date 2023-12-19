#!/usr/bin/python3
"""Square module - includes a Square class to manage the size attribute
and validate its type and value"""


class Square:
    """Defines a square with a private instance attribute 'size'"""

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): Size of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
