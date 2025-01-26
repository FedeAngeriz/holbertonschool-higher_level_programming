#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[replace if elemento == search else elemento for elemento in my_list]
