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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str represantation.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)
