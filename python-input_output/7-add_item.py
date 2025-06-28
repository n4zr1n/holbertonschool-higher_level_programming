#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file in JSON format.

The file used is `add_item.json`. If it already exists,
its contents are loaded and extended with new arguments.
Otherwise, a new list is created.

Functions used:
- save_to_json_file: saves a Python object to a JSON file
- load_from_json_file: loads a Python object from a JSON file
"""

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
