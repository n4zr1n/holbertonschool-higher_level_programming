#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It includes a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A list class that extends the built-in list.

    Methods:
        print_sorted(): Prints the list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order.

        Assumes all elements are integers.
        """
        print(sorted(self))
