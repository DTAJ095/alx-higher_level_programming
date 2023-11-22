#!/usr/bin/python3

"""define a class square"""


class Square:
    """square data

    Attribute:
        size: define the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
            size(int): the size of the new square.
            position(int, int): the position of the new square.
        """
        self.__size = size
        self.__position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets and Sets the position of the new square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the the new square
        Args:
            value: the value to set
        Raise:
            TypeError: if the position is not a tuple of integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)
                or not all(num == "" for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the # char"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
