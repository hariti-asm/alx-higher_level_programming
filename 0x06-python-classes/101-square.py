#!/usr/bin/python3
"""Defines a square bassed on 5-square.py"""


class Square:
    """Represents a square"""

    def __str__(self):
        """Print square."""

        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the current square area"""

        return self.__size * self.__size

    def pos_print(self):
        """Print the square in position"""

        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square in position"""

        print(self.pos_print(), end="")
