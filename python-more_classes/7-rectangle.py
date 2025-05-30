#!/usr/bin/python3
"""Se crea clase Rectangle"""


class Rectangle:
    """Se crea un Rectangle mediante ancho y alto opcionales"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.__height * self.__width

    def perimeter(self):
        if (self.__width or self.__height) == 0:
            return 0
        return (self.__width + self.__height) * 2

    def my_print(self):
        if (self.__width or self.__height) == 0:
            print()
        else:
            for _ in range(self.__height):
                print("#" * (self.__width))

    def __str__(self):
        if self.width == 0 or self.__height == 0:
            return
        p_symbol = str(self.print_symbol)
        return "\n".join(p_symbol * self.__width for i in range(self.__height))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
