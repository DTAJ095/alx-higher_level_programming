#!/usr/bin/python3

""" is_same_class function """


def is_same_class(obj, a_class):
    """ Returns TRUE if the object is exactly an
        instance of the specified class
    """
    return (type(obj) == a_class)
