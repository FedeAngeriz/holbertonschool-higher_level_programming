#!/usr/bin/env python3
from abc import ABC

class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass

        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 
    
    def perimeter(self):
        return 


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimetro: {shape.perimeter()}")
