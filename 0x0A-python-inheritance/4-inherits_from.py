#!/usr/bin/python3
"""Module contains a function that returns true if object is an instance"""


def inherits_from(obj, a_class):
    """This function returns true if object is an instance"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
