#!/usr/bin/env python3


def square_digit(num):
    """num = 765
    cuadrado = num ** 2
    print(cuadrado)"""
    return int(''.join(str(int(digito) ** 2)) for digito in str(num))

    """num_str = str(num)
    result = ""

    for digit in num_str:
        sqr = int(digit) ** 2
        result += str(sqr)
    return int(result)"""