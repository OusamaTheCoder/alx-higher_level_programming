#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Inverts int operators == and !="""
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the != operator"""
        return int(self) == other
