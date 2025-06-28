#!/usr/bin/python3
"""
This module writes a string to a txt file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
