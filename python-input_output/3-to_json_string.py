#!/usr/bin/python3
"""Se importa el modulo json"""

import json


def to_json_string(my_obj):
    """Retorna la representacion json de un objeto"""
    return json.dumps(my_obj)