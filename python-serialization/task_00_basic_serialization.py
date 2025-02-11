#!/usr/bin/python3
"""Basic serialization module that adds the functionality to serialize a Python
dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary"""


import json


def serialize_and_save_to_file(date, filename):
    """Serialize a Python dictionnary to a JSON file"""
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(json.dumps(data))
    pass


def load_and_deserialize(filename):
    """Deserialize the JSON file to recreate the Python dictionnary"""
    with open(filename, "r", encoding="utf-8") as file:
        loaded_data = json.loads(file.read())
    return loaded_data
    pass
