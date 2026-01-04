#!/usr/bin/python3
"""This module represents operations with files"""
import json


def from_json_string(my_str):
    """This function returns object repr"""
    return json.loads(my_str)
