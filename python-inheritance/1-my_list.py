#!/usr/bin/python3
"""
This module prints the list in sorted order.
"""


class MyList(list):
    """
    MyList inherits from built-in list, adds method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
