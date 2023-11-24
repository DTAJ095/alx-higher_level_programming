#!/usr/bin/python3

""" This is the say_my_name module
    It provides a function that print the name of a person
"""


def say_my_name(first_name, last_name=""):
    """Prints my name
        Args:
            first_name(string)
            last_name(string)
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
