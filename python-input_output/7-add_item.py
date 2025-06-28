#!/usr/bin/python3
"""
Module adds all command-line arguments to list and saves it in a JSON file.

If the file already exists, the content is extended with new arguments.
The list is saved in a file called 'add_item.json'.
"""

import sys
import json
from os.path import exists


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
