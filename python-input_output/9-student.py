#!/usr/bin/python3
"""
This module defines student with first_name, last_name, and age.
"""


class Student:
    """Defines student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of the instance."""
        return self.__dict__
