#!/usr/bin/python3
"""Creamos clase MyList, que hereda una
lista llamada list"""


class MyList(list):
    """Imprime una lista ordenada"""
    def print_sorted(self):
        print(sorted(self))
