#!/usr/bin/python3
"""This defines geometric shapes"""


class Square:
    __size = 3
    """This class defines a square"""
    def __init__(self, size=0):
        """This function checks type validation"""
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
