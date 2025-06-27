#!/usr/bin/python3
"""Rectangle class with area and custom string representation"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that validates dimensions and implements area"""

    def __init__(self, width, height):
        """Constructor that validates and sets dimensions"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return custom string representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
