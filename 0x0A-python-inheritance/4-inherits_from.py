#!/usr/bin/python3

""" inherits_from function """


def inherits_from(obj, a_class):
    """ Returns TRUE if the object is an instance of a class
        that inherited(directly/indirectly) from the
        specified class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
