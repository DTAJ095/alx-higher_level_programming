#!/usr/bin/python3

""" Define the lookup function
    returns the list of available attributes and method
    of an object
"""


def lookup(obj):
    """ Returns list of attributes and method """
    return dir(obj)
