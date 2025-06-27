#!/usr/bin/python3
"""
Module with Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Validates the size and calculates area.
    """

    def __init__(self, size):
        """
        Initialize a square with validated size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return string representation of square.
        """
        return f"[Square] {self.__size}/{self.__size}"
