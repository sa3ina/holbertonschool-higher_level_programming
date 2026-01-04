#!/usr/bin/python3
"""This module represents operations with files"""


def write_file(filename="", text=""):
    """This function writes inside file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
