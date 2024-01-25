#!/usr/bin/python3

"""A square class"""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Initalisation

        Arg:
           size: size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
