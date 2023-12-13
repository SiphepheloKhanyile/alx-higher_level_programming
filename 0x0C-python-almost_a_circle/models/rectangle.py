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
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
