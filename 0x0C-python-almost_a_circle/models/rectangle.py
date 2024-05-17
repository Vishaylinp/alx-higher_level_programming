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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("y must ba an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Rectangle with hashes"""
        for y in range(self.y):
            print("")
        for r in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String of rectangle"""
        return (
             f"[Rectangle] ({self.id}) "
             f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Update class
        Args: *arg: arguements
              *Kwargs: key value pairs
        """
        if args and len(args) != 0:
            list_a = ["id", "width", "height", "x", "y"]
            for attr, v in zip(list_a, args):
                setattr(self, attr, v)

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return dict"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
