#!/usr/bin/python3

"""Define a Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectangle"""

    def __init__(self, width, height):
        """initialisation

        Args:
            width: width
            height: height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
