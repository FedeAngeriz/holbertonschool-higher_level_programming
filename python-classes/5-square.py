#!/usr/bin/python3
"""Se define clase Square"""


class Square:
    """Se define un Square mediante la clase anteerior"""
    def __init__(self, size=0):
        """ Se inicializa Square con tamaño opcional.

            size (int): por defecto 0. """

        self.size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        return self.__size ** 2

    def my_print(self):
        if self.__size:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
