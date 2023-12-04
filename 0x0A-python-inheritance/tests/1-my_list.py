#!/usr/bin/python3
"""Module for a a class MyList that inherits from list"""


class MyList(list):
    """class that inherits from 'list'"""
    def __init__(self, lst=[]):
        """Initialising object"""
        super().__init__(lst)
        self.lst = lst

    @property
    def lst(self):
        """getter and setter for lst"""
        return lst

    @lst.setter
    def lst(self, value):
        self.__lst = value

    def print_sorted(self):
        """function that prints the list, sorted (ascending sort)"""
        print(sorted(self))
