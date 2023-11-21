#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data"""

    def __init__(self, szie=0):
        """initialize a new square
        Args:
            size(int): the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get and set the size of the square"""
        return (self.__size)

    @property.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be integer")
        elif (value < 0):
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return(self.__size * self.__size)
