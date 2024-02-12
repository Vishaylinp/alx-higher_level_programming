#!/usr/bin/python3

"""Read file"""


def read_file(filename=""):
    """Reads a text file and prints it"""
    with open(filename, 'r', encoding="utf-8") as open_f:
        print(open_f.read(), end="")
