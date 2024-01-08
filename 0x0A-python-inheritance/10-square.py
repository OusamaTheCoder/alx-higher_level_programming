#!/usr/bin/python3
'''Class Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square.'''
    def __init__(self, size):
        '''__init__.'''
        super().__init__(size, size)

    def __str__(self):
        '''__str__.'''
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

    def area(self):
        '''area.'''
        return self._Rectangle__width * self._Rectangle__height
