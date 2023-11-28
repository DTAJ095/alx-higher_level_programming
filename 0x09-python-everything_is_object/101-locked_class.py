#!/usr/bin/python3
""" Define class LockedClass """


class LockedClass:
    """ class attribute """
    
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
