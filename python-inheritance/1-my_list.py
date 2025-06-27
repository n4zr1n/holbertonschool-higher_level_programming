#!/usr/bin/python3
"""
This module defines a subclass of list with a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList inherits from built-in list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original list.
        """
        print(sorted(self))
