#!/usr/bin/python3
"""This module represents Square"""


Square = __import__('10-square').Square


class Square(Rectangle):
    """This class represents Square inherited from Rectangle"""

    def __init__(self, size):
        """This function checks size"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This function calculates area of square"""

        return self.__size * self.__size

    def __str__(self):
        """This is string representation"""

        return "[Square {}/{}".format(self.__size, self.__size)
