#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """This function adds attributes to objects"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
