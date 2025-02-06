#!/usr/bin/python3
"""Creamos funcion is_same_class"""


def is_same_class(obj, a_class):
    """Retorna True si el objeto es exactamente
    una instancia de la clase especificada,
    de lo contrario devuelve False"""
    return type(obj) is a_class
