#!/usr/bin/python3

""" Defines BaseGeometry class """


class BaseGeometry:
    """ class attributes """
    def area(self):
        """ Returns the area """
        raise Exception("area() is not implemented")
