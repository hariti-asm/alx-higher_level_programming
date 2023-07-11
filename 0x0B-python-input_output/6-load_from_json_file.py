#!/usr/bin/python3
"""Module that creates a Python object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates a Python object from a JSON file"""

    with open(filename) as f:
        return json.load(f)
