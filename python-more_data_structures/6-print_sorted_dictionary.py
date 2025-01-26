#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = a_dictionary.keys()
    sorted(l)
    for k in l:
        print("{}: {}".format(k, a_dictionary[k]))
