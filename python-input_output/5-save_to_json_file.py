#!/usr/bin/python3
"""This module represents operations with files"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes obj to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
