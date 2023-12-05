#!/usr/bin/python3

""" Define a class Student """


class Student:
    """ Student attirbutes:
            -first_name
            -last_name
            -age
    """
    def __init__(self, first_name, last_name, age):
        """ initialize a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary representation of Student
            instance
        """
        return (self.__dict__)
