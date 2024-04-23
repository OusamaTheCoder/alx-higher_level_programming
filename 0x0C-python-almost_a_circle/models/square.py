#!/usr/bin/python3
"""
This is the "Square" module.
This module provides a simple Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square object.

        Args:
        - size (int): The size of the new Square.
        - x (int): The x-coordinate of the new Square. Defaults to 0.
        - y (int): The y-coordinate of the new Square. Defaults to 0.
        - id (int): The identity of the new Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square with new attributes."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)
