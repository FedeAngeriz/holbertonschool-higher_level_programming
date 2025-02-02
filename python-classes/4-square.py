#!/usr/bin/python3
"""Se crea una clase llamada Square"""


class Square:
    """Se define un Square mediante la clase anteerior"""
    def __init__(self, size=0):
        """ Se inicializa Square con tamaño opcional.

            size (int): por defecto 0. """
        self.size = size

    @property
    def size(self):
        """Retorna el tamaño de Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece un nuevo valor para el
        tamaño de Square"""
        if not isinstance(value, int):
            """value (int) Nuevo tamaño de Square"""
            raise TypeError("size must be an integer")
            """TypeError: Si size no es un entero"""
        if value < 0:
            raise ValueError("size must be >= 0")
            """ValueError: Si size es menor que 0"""
        self.__size = value

    def area(self):
        """ Calcula y devuelve el área

            Returns: Area (size * size) """
        return self.__size ** 2
