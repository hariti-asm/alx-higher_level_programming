#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """This class defines a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of a Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        for k, v in json.items():
            setattr(self, k, v)
