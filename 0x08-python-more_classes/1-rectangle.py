#!/usr/bin/python3

"""
A class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """intialization

        Args:
            height(int):
            width(int):
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """get private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width must be an integer, otherwise raise a TypeError
        if width is less than 0, raise a ValueError"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height must be an integer, otherwise raise a TypeError
        if height is less than 0, raise a ValueError"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

