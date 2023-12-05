#!/usr/bin/python3

""" to_json_string function """


import json


def to_json_string(my_obj):
    """ returns the string representation of an object
        (string)
    """
    return json.dumps(my_obj)
