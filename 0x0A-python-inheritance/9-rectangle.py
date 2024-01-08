#!/usr/bin/python3
'''Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class.'''
    def __init__(self, width, height):
        '''__init__.'''
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        '''Area method.'''
        return self.__width * self.__height

    def __str__(self):
        '''__str__.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
