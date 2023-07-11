#!/usr/bin/python3
"""Module that reads a UTF8 text file and prints it to stdout"""


def read_file(filename=""):
    """Function that reads a UTF8 text file and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
