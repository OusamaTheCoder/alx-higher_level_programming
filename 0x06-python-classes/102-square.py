#!/usr/bin/python3
"""Square module - defines a square and comparison methods"""


class Square:
    """Represents a square and comparison methods based on area."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance.

        Args:
            size: Length of each side of the square.
            position: Coordinates to locate the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of the square."""
        return pow(self.__size, 2)

    @property
    def size(self):
        """Getter and setter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): Size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __eq__(self, other):
        """Defines the == comparison for Square objects based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison for Square objects based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison for Square objects based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison for Square objects based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison for Square objects based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison for Square objects based on area."""
        return self.area() >= other.area()
