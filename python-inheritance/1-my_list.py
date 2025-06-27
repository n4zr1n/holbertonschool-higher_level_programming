#!/usr/bin/python3
"""
This module prints the list in sorted order.
"""


class MyList(list):
    """
    MyList adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Example:
        >>> my_list = MyList()
        >>> my_list.append(3)
        >>> my_list.append(1)
        >>> my_list.append(2)
        >>> my_list.print_sorted()
        [1, 2, 3]
        >>> print(my_list)
        [3, 1, 2]
        """
        print(sorted(self))
