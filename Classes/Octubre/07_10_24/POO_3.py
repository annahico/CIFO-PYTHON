# Ejercicio 3 Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.

import math
class circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi*(self.radio)**2

    def perimetro(self):
        return 2*math.pi*self.radio

    def __str__(self):
        return f" Este es un objeto circulo con radio {self.radio}"


circulo1 = circulo(10)
print(circulo1)
print(circulo1.area())
print(circulo1.perimetro())
print(circulo1.radio)
circulo1.radio = 1
print(circulo1)
print(circulo1.area())
print(circulo1.perimetro())
print(circulo1.radio)
