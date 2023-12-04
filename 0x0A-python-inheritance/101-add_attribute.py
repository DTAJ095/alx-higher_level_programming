#!/usr/bin/python3

""" add_attribute function """


def add_attribute(obj, att, value):
    """ Adds a new attribute to an object if possible
        Args:
            obj: the object to add an attribute to.
            att: the attribute to be added.
            value: the value of the attribute.

        Raises:
            TypeError: if the attribute can be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
