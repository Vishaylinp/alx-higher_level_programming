#!/usr/bin/python3

"""Json string"""


def from_json_string(my_str):
    """deserialisation

    Args:
        my_str: string
    """
    import json
    return (json.loads(my_str))
