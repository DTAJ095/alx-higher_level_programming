#!/usr/bin/python3

""" This is the 0-add_integer module
    it suppies the function to add two integers
"""


def add_integer(a, b=98):
    """ Adding two integers
    Args:
        a(int): the fisrt integer
        b(int): the second one
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
