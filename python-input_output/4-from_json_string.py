#!/usr/bin/python3
"""Se importa el modulo json"""

import json


def from_json_string(my_str):
    """Retorna un objeto representado por un string de json"""
    return json.loads(my_str)