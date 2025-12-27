#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) * abs(self.radius)

    def perimeter(self):
        return math.pi * 2 * abs(self.radius)

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
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(3, 5)

    shape_info(c)
    shape_info(r)
