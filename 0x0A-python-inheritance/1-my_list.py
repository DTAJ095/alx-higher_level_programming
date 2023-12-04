#!/usr/bin/python3

""" Defines a class Mylist """


class Mylist:
    """ class attributes """

    def __init__(self):
        """ initialize an object """
        super().__init__()

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
