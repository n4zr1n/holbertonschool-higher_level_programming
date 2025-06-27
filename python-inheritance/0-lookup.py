#!/usr/bin/python3
"""
This module provides a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
