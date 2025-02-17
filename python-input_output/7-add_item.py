#!/usr/bin/python3
"""Se importa modulo sys, json y path"""
import sys
import json
from os import path

"""Agrega todos los argumentos a una lista"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
"""Los guarda en un archivo"""
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
