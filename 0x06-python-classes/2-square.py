#!/usr/bin/python3
"""Defines a square bassed on 1-square.py"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the data"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
