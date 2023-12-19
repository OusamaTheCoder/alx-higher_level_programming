#!/usr/bin/python3
"""Square module - contains a Square class to manage the size attribute,
compute the area, and print a square with '#' characters"""


class Square:
    """Represents a square with a private instance attribute size"""

    def __init__(self, size=0):
        """Constructor to initialize the square.

        Args:
            size: Length of the side of a square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of the size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size attribute.

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

    def my_print(self):
        """Prints the square to stdout using '#' characters."""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()
