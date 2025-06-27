#!/usr/bin/python3
"""
This module provides a function to check if an object
is a subclass instance (not same class).
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The parent class.

    Returns:
        True if obj inherits from a_class but is not a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
