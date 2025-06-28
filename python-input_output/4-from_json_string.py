#!/usr/bin/python3
"""
This module returns object
"""


import json
"""importing json"""


def from_json_string(my_str):
    """Returns an object (Python data structure) from a JSON string."""
    return json.loads(my_str)
