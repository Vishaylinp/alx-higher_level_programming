#!/usr/bin/python3
"""Contains a Base class"""


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
