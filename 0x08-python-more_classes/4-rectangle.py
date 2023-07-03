#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle based on 3-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Set width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Set height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute"""""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for n in range(self.__height):
            for m in range(self.__width):
                rectangle += "#"
            if n < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """Return string representation of rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)
