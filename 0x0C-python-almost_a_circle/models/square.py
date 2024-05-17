#!/usr/bin/python3
"""Class of Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initilisation
        Args:
            id : id
            Size: size
            x: x
            y: y
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """set width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """String of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
