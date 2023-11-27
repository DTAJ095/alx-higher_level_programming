#!/usr/bin/python3

""" Defining a class Rectangle """


class Rectangle:
    """ Rectangle's data """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle
            Args:
                width(int): the rectangle's width
                height(int): the rectangle's height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ("")
        _rect = []
        for i in range(self.__height):
            [_rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                _rect.append("\n")
        return ("".join(_rect))

    def __repr__(self):
        """ Returns the string representation of the rectangle
            for a reproduction
        """
        _rect = "Rectangle(" + str(self.__width)
        _rect += ", " + str(self.__height) + ")"
        return (_rect)

    def __del__(self):
        """ Print a message when ever a rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the rectangle with the highest area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new rectangle instance with
            width == height == size
        """
        cls = Rectangle()
        return Rectangle(size, size)
