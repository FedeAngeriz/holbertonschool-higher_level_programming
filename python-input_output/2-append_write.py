#!/usr/bin/python3
"""Funcion que agrega un strings al final del archivo de texto"""


def append_write(filename="", text=""):
    """Retorna la cantidad de caracteres agregados"""
    with open(filename, 'a') as file:
        return file.write(text)
