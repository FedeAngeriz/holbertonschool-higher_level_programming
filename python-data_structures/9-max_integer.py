#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximo = my_list[0]
    for elemento in my_list:
        if elemento > maximo:
            maximo = elemento
    return maximo
