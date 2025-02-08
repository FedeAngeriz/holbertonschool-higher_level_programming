#!/usr/bin/python3
"""Creamos clase BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Creamos clase Rectangle, que hereda BaseGeometry"""

class Rectangle(BaseGeometry):
    """Se define un rectangulo con alto y ancho validados"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
