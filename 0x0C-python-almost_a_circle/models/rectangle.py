#!/usr/bin/python3
"""Contains subclass of base"""
from models.base import Base


class Rectangle(Base):
    """initialisation
    Args:
        width: width
        height: height
        x: x
        y: y
        id: id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of attr
        Arg:
            value: value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for attr
        Arg:
            value: height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for attr
        Arg:
            value: x value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for attr
        Arg:
            value: x value
        """
        if type(value) != int:
            raise TypeError("y must ba an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle"""
        return self.width * self.height
