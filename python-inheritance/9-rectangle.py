#!/usr/bin/python3
"""This module represents Geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents rectangle"""

    def __init__(self, width, height):
        """This function initializes a rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This function calculates area"""

        return self.__width * self.__height

    def __str__(self):
        """This is string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
