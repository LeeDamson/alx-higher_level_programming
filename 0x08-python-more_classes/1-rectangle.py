#!/usr/bin/python3

"""An empty class Rectangle that defines a rectangle:"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """Private instance attributes: width(int), height(int)"""
        self.__width = width
        self.__height = height

        """property def width(self): to retrieve it"""
    @property
    def width(self):
        return self.__width

        """property def height(self): to retrieve it"""
    @property
    def height(self):
        return self.__height

        """property setter def width(self, value): to set it"""
    @width.setter
    def width(self, value):
        """width must be an integer, otherwise raise a TypeError exception with the message width must be an integer"""
        if not isintstance(value, int):
            raise TypeError("width must be an integer")
        """if width is less than 0, raise a ValueError exception with the message width must be >= 0"""
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        """property setter def height(self, value): to set it"""
    @height.setter
    def width(self, value):
        """height must be an integer, otherwise raise a TypeError exception with the message height must be an integer"""
        if not isintstance(value, int):
            raise TypeError("height must be an integer")
        """if height is less than 0, raise a ValueError exception with the message height must be >= 0"""
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
