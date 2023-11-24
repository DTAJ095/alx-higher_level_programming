#!/usr/bin/python3


""" This is the text_indentation module
    It provides a function that print a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Print a text
        Args:
            text(string)
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
