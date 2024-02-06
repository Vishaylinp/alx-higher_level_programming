#!/usr/bin/python3

"""Function to check inherite"""


def inherits_from(obj, a_class):
    """inherits from superclass

    Args:
        obj: object
        a_class: class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
