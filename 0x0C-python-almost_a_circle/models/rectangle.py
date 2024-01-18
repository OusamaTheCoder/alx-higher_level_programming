#!/usr/bin/python3
"""This module contains the Rectangle class."""


class Rectangle(Base):
    """This class represents a rectangle."""
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
