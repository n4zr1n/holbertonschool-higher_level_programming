#!/usr/bin/python3
"""
This module defines MyList class.

>>> my_list = MyList([3, 1, 4])
>>> my_list.print_sorted()
[1, 3, 4]
>>> print(my_list)
[3, 1, 4]
"""


class MyList(list):
    """
    MyList extends list to add a print_sorted method.
    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))
