#!/usr/bin/python3

"""Define square that inherits from REctangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent square"""

    def __init__(self, size):
        """initialisation

        Arg:
           size: size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
