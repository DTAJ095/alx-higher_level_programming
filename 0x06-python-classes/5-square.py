#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data

    Attribute:
        size: define the size of the square
    """

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): the size of the new square.
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

    def my_print(self):
        """prints a square with # character"""

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
