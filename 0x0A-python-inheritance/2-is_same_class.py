#!/usr/bin/python3

"""Check if object is a instance"""


def is_same_class(obj, a_class):
    """return True if object isinstance

    Args:
        Obj: object
        a_class: class to check
    """

    return (type(obj) == a_class)
