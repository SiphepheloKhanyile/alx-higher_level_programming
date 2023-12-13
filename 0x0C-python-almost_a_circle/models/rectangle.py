#!/usr/bin/python3
"""
Module for Class 'Rectangle' that inherits from Class 'Base'.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing Rectangle object.
        Args:
            width (int) : width of Rectangle
            height (int) : height of Rectangle
            x (int) : default = 0
            y (int) : default = 0
            id (int) : default = 0
        """
        super().__init__(id)
        if (isinstance(width, int) is False):
            raise TypeError("width must be an integer")
        if (isinstance(height, int) is False):
            raise TypeError("height must be an integer")
        if (isinstance(x, int) is False):
            raise TypeError("x must be an integer")
        if (isinstance(y, int) is False):
            raise TypeError("y must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter and setter fot width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
