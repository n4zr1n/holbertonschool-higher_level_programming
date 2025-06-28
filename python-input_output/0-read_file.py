#!/usr/bin/python3
"""
This module creates a function to read and print txt file.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
