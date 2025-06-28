#!/usr/bin/python3
"""
this module  adds all arguments to a Python list
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
