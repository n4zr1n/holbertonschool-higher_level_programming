#!/usr/bin/python3
"""
This module inherits from built-in list.
"""


class MyList(list):
    """
    A list class prints a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
