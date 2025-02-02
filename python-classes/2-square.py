#!/usr/bin/python3
"""Se crea una clase, llamada Square"""


class Square:

    def __init__(self, size=0):
        """Se inicializa Square con un tamaño opcional
        size (int): por defecto es 0"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """TypeError: Si size no es un entero"""
        if size < 0:
            raise ValueError("size must be >= 0")
            """ValueError: Si size es menor que 0"""
        self.__sizeof__ = size
