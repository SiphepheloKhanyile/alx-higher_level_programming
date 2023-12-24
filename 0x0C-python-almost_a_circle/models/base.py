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
        Args:
            list_dictionaries(dict): List of dictionaries
        Return:
            JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of list_objs to a file
        Args:
            list_objs(list): list of instances who inherits from base
        """
        if list_objs is None:
            filename = str(type(cls).__name__) + ".json"
            with open(filname, "w+") as ef:
                ef.write(list())
        else:
            filename = str(type(cls).__name__) + ".json"
            with open(filename, "w+") as ef:
                ef.write(cls.to_json_string(list_objs))
