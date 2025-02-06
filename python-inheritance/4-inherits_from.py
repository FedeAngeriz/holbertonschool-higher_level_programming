#!/usr/bin/python3
"""Creamos funcion inherits_from"""

def inherits_from(obj, a_class):
    """Retorna True si el objeto es una instancia de
    una clase especifica que heredo, directa o
    indirectamente, de lo contrario False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
