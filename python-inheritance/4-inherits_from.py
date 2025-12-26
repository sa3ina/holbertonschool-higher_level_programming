#!/usr/bin/python3
"""This module represents inheritance"""


def inherits_from(obj, a_class):
    """This class returns true if object is instance of specified class"""

    return isinstance(obj, a_class) and type(obj) is not a_class
