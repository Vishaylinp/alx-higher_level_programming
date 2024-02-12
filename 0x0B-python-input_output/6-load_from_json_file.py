#!/usr/bin/python3

"""create object"""
import json


def load_from_json_file(filename):
    """Creates object fdrom json file

    Args:
        filename: filename
    """
    with open(filename, 'r') as r_f:
        return json.load(my_obj, r_f)
