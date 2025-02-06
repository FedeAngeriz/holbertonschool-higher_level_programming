#!/usr/bin/python3
"""Creamos funcion is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Retorna True si el objeto es una instancia
    de la clase especificada o de una heredada,
    de lo contrario devuelve False"""
    return isinstance(obj, a_class)
