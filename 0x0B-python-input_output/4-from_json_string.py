#!/usr/bin/python3
"""Module that returns the Python object representation of a JSON string"""
import json


def from_json_string(my_str):
    """Function returns the Python object representation of a JSON string"""

    return json.loads(my_str)
