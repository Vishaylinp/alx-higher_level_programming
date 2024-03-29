#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialisation

        Args:
            width: width of recctangle
            heigh: heigh of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get a private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get a private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of rectsngle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """print a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for column in range(self.__height):
            [rectangle.append('#') for row in range(self.__width)]
            if column != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """return recreation of a new instance"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)
