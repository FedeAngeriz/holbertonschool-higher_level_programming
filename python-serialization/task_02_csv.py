#!/usr/bin/env python3
"""Se importan los modulos CSV y JSON"""


import csv
import json


"""Convierte un archivo CSV a JSON y lo guarda en data.json"""
def convert_csv_to_json(filename_csv):
    try:
        with open(filename_csv, 'r') as file_csv:
            leer = csv.DictReader(file_csv)
            datos = list(leer)

        with open('data.json', 'w') as file_json:
            json.dump(datos, file_json)
        return True

    except FileNotFoundError:
        print(f"Error: File '{file_csv}'not found.")
        return False
    except Exception as error:
        print(f"Error convertir CSV to JSON: {error}")
        return False
