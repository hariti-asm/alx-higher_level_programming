#!/usr/bin/python3
"""Defines a square bassed on 3 -square.py"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data"""

        self.size = size

    @property
    def size(self):
        """Retrieve size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets Size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Return the current square area"""

        return (self.__size * self.__size)
