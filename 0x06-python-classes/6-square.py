#!/usr/bin/python3
"""Square module - contains a Square class to manage the size
attribute, position,and print a square with '#' characters"""


class Square:
    """Represents a square with private instance attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor to initialize the square.

        Args:
            size: Length of the side of a square.
            position: Tuple representing the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size.

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

    @property
    def position(self):
        """Retrieves the value of position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position.

        Args:
            value: Tuple representing the position (x, y).

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout using '#' characters."""

        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
