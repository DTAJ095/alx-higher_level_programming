#!/usr/bin/python3

import math


"""define a MagicClass matching with a Python bytecode"""


class MagicClass:
    """Define a circle"""

    def __init__(self, radius=0):
        """initialize the magicClass"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Rteurn the area of the MagicClass"""
        return (self.__radius**2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass"""
        return (self.__radius * 2 * math.pi)
