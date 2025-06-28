#!/usr/bin/python3
"""
This module defines a Student class.

The `to_json` allows selective or full attribute export depending on
whether a list of attribute names is provided.
"""


class Student:
    """Defines student with first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the instance.

        If `attrs` is list of strings, only those attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
