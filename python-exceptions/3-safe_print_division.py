#!/usr/bin/python3
def safe_print_division(a, b):
    resultado = 0
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = None
        return None
    finally:
        print("Inside result: {}".format(resultado))
    return resultado
