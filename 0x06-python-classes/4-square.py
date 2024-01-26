#!/usr/bin/python3

"""A square class"""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Initialisation

        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """get private attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setter for private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square"""
        return(self.__size * self.__size)
