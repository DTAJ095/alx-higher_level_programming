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

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of Student
            instance
        """
        if attrs is None:
            return (self.__dict__)
        my_dict = {}
        for x in attrs:
            try:
                my_dict[x] = self.__dict__[x]
            except:
                pass
        return (my_dict)
