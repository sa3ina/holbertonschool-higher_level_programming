#!/usr/bin/python3
"""This module represents operations with files"""
import json


def load_from_json_file(filename):
    """This function creates object from JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
