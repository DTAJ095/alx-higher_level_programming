#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data

    Attribute:
        size(int): defines the size of the square
    """

    def __init__(self, size=0):
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
        """Sets the size private attribute value.

        Args:
            value: the value to set

        Raises:
            TypeError: if the size is not an integer
            ValueError: if size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """define <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define >= comparison"""
        return self.area() >= other.area()
