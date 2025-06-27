#!/usr/bin/python3
"""Module with BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with basic geometry methods"""

    def area(self):
        """Raise exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
