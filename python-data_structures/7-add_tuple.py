#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista = [0, 0]
    for i in range(len(tuple_a)):
        lista[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        lista[i] += tuple_b[i]
    return tuple(lista)
