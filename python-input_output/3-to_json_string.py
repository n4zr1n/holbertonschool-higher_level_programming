#!/usr/bin/python3
"""
This module returns json representation
"""


import json
"""importing json"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
