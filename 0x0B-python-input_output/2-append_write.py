#!/usr/bin/python3

""" append_write function """


def append_write(filename="", text=""):
    """ appends a string to a text file """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
