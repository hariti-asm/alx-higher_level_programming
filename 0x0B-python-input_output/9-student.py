#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """This class defines a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of a Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance"""

        return self.__dict__
