#!/usr/bin/python3

"""return true if the object is an instance of"""


def is_kind_of_class(obj, a_class):
    """return true if object is an instance of class

    Args:
        obj: object
        a_class: class
    """
    return (isinstance(obj, a_class))
