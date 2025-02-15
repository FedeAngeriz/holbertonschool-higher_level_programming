#!/usr/bin/python3
"""Funcion read_file, lee un archivo de texto"""


def read_file(filename=""):
    """abre el archivo y lo imprime en salida estandar"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
