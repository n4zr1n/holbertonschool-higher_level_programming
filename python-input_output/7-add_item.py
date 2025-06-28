#!/usr/bin/python3
"""
Module that adds all command-line arguments to a Python list
and saves them to a file in JSON format.

The list is saved in 'add_item.json'. If the file exists, it
loads the existing list and appends new arguments.
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
