#!/usr/bin/python3
"""writing a class"""
import math


class MagicClass:
    """Setting up the class"""

    def __init__(self, radius=0):
        """Setting up the init"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Such docstring"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Such docstring"""

        return 2 * math.pi * self.__radius
