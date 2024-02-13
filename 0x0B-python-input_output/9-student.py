#!/usr/bin/python3

"""student class"""


class Student:
    """Create a student class"""

    def __init__(self, first_name, last_name, age):
        """initialisation

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary"""
        return self.__dict__
