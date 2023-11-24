#!/usr/bin/python3
"""Final mode for module that defines a square class"""


class Square():
    """a class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialising square object
        Args:
            size(int): size of square, deafualt = 0
            position(tuple): optional positional arguement
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter and setter for 'size'"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter and setter for 'position'"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """print square using '#' symbols"""
        if (self.__size == 0):
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
