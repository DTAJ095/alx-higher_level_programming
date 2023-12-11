#!/usr/bin/python3

""" Define a class Base """
import json
import csv
import turtle


class Base():
    """ Base model
        represent the base of all other classes we will be
        using for this project

    Private Class Attribute:
       __nb_objects(int): number of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """ Returns the JSON serialization of a list of dict
        """
        if list_dict is None or list_dict == []:
            return ("[]")
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_obj):
        """ Write the JSON representation of a list of objects
        to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_obj is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_obj]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ return the deserialization of a JSON string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return a class instantied from a dictionary
        of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cls = cls(1, 1)
            else:
                new_cls = cls(1)
            new_cls.update(**dictionary)
            return (new_cls)

    @classmethod
    def load_from_file(cls):
        """ Return a list of classes instantiated from a file
        of JSON string
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.form_json_string(f.read())
                return ([cls.create(**dict) for dict in list_dicts])
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_obj):
        """ Write a csv representation of a list of objects to a file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", new_line="") as csv_file:
            if list_obj is NOne or list_obj == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    _field = ['id', 'width', 'height', 'x', 'y']
                else:
                    _field = ['id', 'size', 'x', 'y']
                wrt = csv.DictWriter(csv_file, _field=_field)
                for obj in list_obj:
                    wrt.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of class instantiated from a CSV file

        Reads from `<cls.__name__>.csv

        Returns: list of classes or empty list ortherwise
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    _field = ['id', 'width', 'height', 'x', 'y']
                else:
                    _field = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(csv, _field=_field)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5f3d8i")
        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
