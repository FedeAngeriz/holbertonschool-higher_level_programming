#!/usr/bin/python3
def roman_to_int(roman_string):
    list_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    prev = 0
    for number_r in roman_string[::-1]:
        number = list_r[number_r]

        if number < prev:
            resultado -= number
        else:
            resultado += number
        prev = number
    return resultado
