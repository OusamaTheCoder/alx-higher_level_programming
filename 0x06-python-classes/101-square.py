#!/usr/bin/python3
"""Square module"""

class Square:
    """Represents a square"""

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
        """Setter for the size attribute."""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Getter and setter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        i, j = value
        if isinstance(i, int) and isinstance(j, int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if i < 0 or j < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints a visual representation of the square."""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0):
                    if i != 0:
                        print()
                    for i in range(self.__position[0]):
                        print(' ', end='')
                print('#', end='')

    def __str__(self):
        """String representation of the square."""
        Square.my_print(self)
        return ""
