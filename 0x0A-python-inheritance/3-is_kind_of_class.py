#!/usr/bin/python3

""" is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ Returns TRUE if the object is an instance
    of object or inhirited from it

    """
    return (isinstance(obj, a_class))
