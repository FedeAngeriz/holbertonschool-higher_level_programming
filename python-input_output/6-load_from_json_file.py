#!/usr/bin/python3
"""Se importa el modulo json"""

import json


def load_from_json_file(filename):
    """Se crea un objeto a partir de un archivo json"""
    with open(filename, 'r', encoding="") as file:
        return json.load(file)
