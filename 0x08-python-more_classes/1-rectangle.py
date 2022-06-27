#!/usr/bin/python3
"""1-rectangle Module
Defines a rectangle with
an input height and width
"""
class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            """Returns a typeerror if NaN"""
            raise TypeError("width must be an integer")
        elif value < 0:
            """Returns a valueerror if value is less than 0"""
            raise ValueError("width must be >= 0")
        else:
            """Sets the width value"""
            self.__width = value

    @property
    def height(self):
        """Returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            """returns a typeerror if value is NaN"""
            raise TypeError("height must be an integer")
        elif value < 0:
            """returns a valueerror if value is less than 0"""
            raise ValueError("height must be >= 0")
        else:
            """sets the height value"""
            self.__height = value
