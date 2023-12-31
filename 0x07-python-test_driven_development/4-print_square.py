#!/usr/bin/python3


""" This is the print_square module
    It provides a function that prints a square with
    the # character
"""


def print_square(size):
    """Prints a square
        Args:
            size(int): the size of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
