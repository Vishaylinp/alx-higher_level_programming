#!/usr/bin/python3

"""Empty class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area with exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation

        Args:
            name: string
            value: value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
