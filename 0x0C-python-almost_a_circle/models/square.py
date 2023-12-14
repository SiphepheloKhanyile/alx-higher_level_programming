#!/usr/bin/python3
"""
Class 'Square' that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Inititializing Square oobject
        Args:
            size (int): size of square
        """
        self.__size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        str represantation.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)
