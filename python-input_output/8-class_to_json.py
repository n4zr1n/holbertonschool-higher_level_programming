#!/usr/bin/python3
"""
This module returns dictionary description
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization."""
    return obj.__dict__
