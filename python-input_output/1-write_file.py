#!/usr/bin/python3
"""Funcion write_file, que escribe un string en un archivo de texto"""


def write_file(filename="", text=""):
    """Retorna la cantidad de caracteres escritos"""
    with open(filename, 'w') as file:
        return file.write(text)
