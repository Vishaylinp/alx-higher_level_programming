#!/usr/bin/python3

"""Class that inherits list"""


class MyList(list):
    """print the list"""

    def print_sorted(self):
        """print in ascending"""
        print(sorted(self))
