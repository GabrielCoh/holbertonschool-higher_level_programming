#!/usr/bin/python3
"""The JSON representation"""


import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
