#!usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
Private instance attribute: width
Private instance attribute: height
Instantiation with optional width and height: def __init__(self, width=0, height=0):
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def set_width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def set_height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        r1 = Rectangle(80, 140)
