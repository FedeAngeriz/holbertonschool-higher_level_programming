#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    clave = list(a_dictionary.keys())
    clave.sort()
    for k in clave:
        print("{}: {}".format(k, a_dictionary[k]))
