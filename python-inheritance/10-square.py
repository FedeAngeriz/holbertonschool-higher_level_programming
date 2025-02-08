#!/usr/bin/python3
"""Creamos clase BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Creamos clase Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

"""Creamos clase Square que hereda Rectangle"""


class Square(Rectangle):
    """Se define un cuadrado"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        return self.__size * self.__size
