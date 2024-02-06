#!/usr/bin/python3

"""returns list of available attributes"""


def lookup(obj):
    """"Lookup"""
    return list(dir(obj))
