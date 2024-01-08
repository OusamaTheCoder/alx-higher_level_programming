#!/usr/bin/python3
'''Module for Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class for Square.'''
    def __init__(self, size):
        '''Method for initialization.'''
        super().__init__(size, size)

    def area(self):
        '''Method for area.'''
        return super().area()

    def __str__(self):
        '''Method for string representation.'''
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
