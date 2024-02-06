#!/usr/bin/python3

"""Class that inherits list"""


class MyList(list):
    """print the list"""

    def __init__(self):
        """initilaisation"""
        super().__init__()

    def print_sorted(self):
        """print in ascending"""
        print(sorted(self))
