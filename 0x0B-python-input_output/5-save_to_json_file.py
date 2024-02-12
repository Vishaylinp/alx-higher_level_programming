#!/usr/bin/python3

"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to file

    Args:
        filename: filename
        my_obj: object
    """
    with open(filename, 'w') as wr_f:
        json.dump(my_obj, wr_f)
