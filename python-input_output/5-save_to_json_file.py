#!/usr/bin/python3
"""Se importa el modulo json"""

import json


def save_to_json_file(my_obj, filename):
    """Escribe un objeto en un archivo usando json"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj), end="")