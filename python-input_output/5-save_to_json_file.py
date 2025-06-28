#!/usr/bin/python3
"""
This module writes object to a text file.
"""


import json

"""importing json"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
