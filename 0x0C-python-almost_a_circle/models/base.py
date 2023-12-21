#!/usr/bin/python3
"""
Module to define Class 'Base'
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON str representation of list_dictionaries
        """
        if ((list_dictionaries is None) or (list_dictionaries is "")):
            return "[]"
        json_str_repr = json.dumps(list_dictionaries)
        return json_str_repr
