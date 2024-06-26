#!/usr/bin/python3
"""Contains a Base class"""
import json


class Base:
    """A base Model

    private class atrribute:
    __nb_objects: private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation
        Args:
            id: identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json string
        Args:
            json_string: A Json string
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)
