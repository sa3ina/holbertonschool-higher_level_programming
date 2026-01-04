#!/usr/bin/python3
"""This module represents operations with files"""
import json


def to_json_string(my_obj):
    """This function returns the JSON repr"""
    return json.dumps(my_obj)
