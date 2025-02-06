#!/usr/bin/python3
"""Creamos clase BaseGeometry"""


class BaseGeometry:
    """Metodo que debe ser implementado en las subclases"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

"""Creamos clase Rectangle, que hereda BaseGeometry"""

class Rectangle(BaseGeometry):
    """Se define un rectangulo con alto y ancho definidos"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Devuelve area de rectangulo"""
        return self.width * self.height
    
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
