#!/usr/bin/python3
"""Module with Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that validates width and height"""

    def __init__(self, width, height):
        """Initialize rectangle and validate dimensions"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
