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
        my_dict = dict()
        if attrs and all(isinstance(x, str) for key in attrs):
            for key in attrs:
                if key in self.__dict__:
                    my_dict.update({key: self.__dict__[key]})
            return (my_dict)
        return self.__dict__


    def reload_from_json(self, json):
        """ Replace all attributes of the Student instance """
        for key in json:
            self.__dict__.update({key: json[key]})
