#!/usr/bin/python3
"""
This module defines the Square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
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

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)
