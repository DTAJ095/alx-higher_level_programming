#!/usr/bin/python3

""" Defines BaseGeometry class """


class BaseGeometry:
    """ class attributes """
    def area(self):
        """ Returns the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be grater than 0".format(name))
