#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data"""

    def __init__(self, size=0):
        """Initiaize a new square
        Args:
            size(int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
