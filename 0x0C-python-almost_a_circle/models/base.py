#!/usr/bin/python3
"""
Module to define Class 'Base'
"""


class Base:
    """
    Base class for all other classes for this peoject.
    Attributes:
        __nb_objects (int) : number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing object.
        Args:
            id (int) : object id
        """
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
