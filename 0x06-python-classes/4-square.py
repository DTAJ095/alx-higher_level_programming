#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data"""

    def __init__(self, szie=0):
        """initialize a new square
        Args:
            size(int): the size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get and set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
