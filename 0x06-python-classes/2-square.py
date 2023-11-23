#!/usr/bin/python3
"""Continuation of a module that defines Square class"""


class Square():
    """class that defines a square"""
    def __init__(self, size=0):
        """Initializing Square class object
        Args:
            size(int): size of square, default to 0
        """
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
