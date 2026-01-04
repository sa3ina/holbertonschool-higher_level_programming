#!/usr/bin/python3
"""This module represents operations with files"""


def append_write(filename="", text=""):
    """This function appends text into file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
