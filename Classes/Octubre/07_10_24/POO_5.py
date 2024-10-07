# Ejercicio 5
# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

import math

class triangulo:
    def __init__(self, lado1, lado2, lado3) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def estriangulo(self):
        if (self.lado1 >= self.lado2 + self.lado3) or (self.lado2 >= self.lado1 + self.lado3) or (self.lado3 >= self.lado1 + self.lado2):
            return False
        else:
            return True

    def mayor(self):
        if self.lado1 >= self.lado2 and self.lado2 >= self.lado3:
            return self.lado1
        elif self.lado2 >= self.lado1 and self.lado1 >=self.lado3:
            return self.lado2
        else:
            return self.lado3
        
    def tipo(self):
        if (self.lado1 != self.lado2) and (self.lado1 != self.lado3) and (self.lado2 != self.lado3):
            return "El triangulo es Escaleno"
        elif (self.lado1 == self.lado2) and (self.lado2 == self.lado3):
            return "El triangulo es Equilatero"
        else:
            return "El triangulo es Isosceles"
        
    def __str__(self) -> str:
        return f"Este es un objeto triangulo con lados {self.lado1},{self.lado2},{self.lado3}"
    

triangulo1 = triangulo(7,1,0)
print(triangulo1)
print(triangulo1.mayor())
print(triangulo1.tipo())