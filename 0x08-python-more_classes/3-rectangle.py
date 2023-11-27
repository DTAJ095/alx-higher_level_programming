#!/usr/bin/python3

""" Defining a class Rectangle """


class Rectangle:
    """ Rectangle's data """

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle
            Args:
                width(int): the rectangle's width
                height(int): the rectangle's height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gest and sets the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ gets the value of the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets and sets the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Gets the value of the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns the printable string representation of
            the rectangle
        """
        string = ""
        if self.__width != 0 and self.height != 0:
            string += "\n".join("#" *self.__width
                    for i in range(self.__height))
        return (string)
