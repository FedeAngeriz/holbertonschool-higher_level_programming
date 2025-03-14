#!/usr/bin/env python3
"""Se importa modulo pickle"""


import pickle


"""Guardamos y recuperamos objetos con sus atributos y metodos, sin tener que volver a crearlos"""
class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as error:
            print(f"Error al serializar objeto: {error}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as error:
            print(f"Error deserializando objeto: {error}")
            return None
