#!/usr/bin/python3
def no_c(my_string):
    new_cadena = ""
    for i in my_string:
        if i.lower() != "c":
            new_cadena += i
    return new_cadena
