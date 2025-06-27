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
    """ MyList class inherits from list and includes print_sorted method """

    def __init__(self, *args):
        """ Instantiates the MyList object """
        super().__init__(*args)

    def print_sorted(self):
        """ Prints the list sorted in ascending order """
        print(sorted(self))

    def __str__(self):
        """ Returns a string representation of the list """
        return f"[{', '.join(map(str, self))}]"
