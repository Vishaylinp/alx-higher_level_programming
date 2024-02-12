#!/usr/bin/python3

"""JSON string"""


def to_json_string(my_obj):
    """serialisation

    Args:
        my_obj: object string
    """

    import json
    return (json.dumps(my_obj))
