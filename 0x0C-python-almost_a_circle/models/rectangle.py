#!/usr/bin/python3
"""Header"""


from models.base import Base


class Rectangle(Base):
    """
    This is the Rectangle class, which inherits from the Base class.

    Attributes:
    - __width (int): Private instance attribute for the width.
    - __height (int): Private instance attribute for the height.
    - __x (int): Private instance attribute for the x-coordinate.
    - __y (int): Private instance attribute for the y-coordinate.
    - id (int): Public instance attribute inherited from the Base class.

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None):
    Constructor method to initialize the Rectangle instance.
    - Getter and setter methods for each private attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance.

        Args:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int, optional): x-coordinate of the rectangle (default is 0).
        - y (int, optional): y-coordinate of the rectangle (default is 0).
        - id (int, optional): Object's id. If provided,
        assign it to the id attribute; otherwise,
        call the super class with id to use the logic of the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value