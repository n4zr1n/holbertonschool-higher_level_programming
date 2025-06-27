#!/usr/bin/python3
"""
This module provides a function that checks if an object
is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
