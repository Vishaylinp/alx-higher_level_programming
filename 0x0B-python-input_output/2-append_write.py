#!/usr/bin/python3

"""Append file"""


def append_write(filename="", text=""):
    """Appends a string at the EOF"""
    with open(filename, 'a', encoding="UTF-8") as ap_f:
        return (ap_f.write(text))
