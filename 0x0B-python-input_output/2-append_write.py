#!/usr/bin/python3
"""Module that appends a string to the end of a UTF8 text file"""


def append_write(filename="", text=""):
    """Function that appends a string to the end of a UTF8 text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
