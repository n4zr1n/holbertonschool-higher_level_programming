#!/usr/bin/python3
"""
This module provides a function to check if an object is an
instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of or inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is instance or subclass, else False.
    """
    return isinstance(obj, a_class)
