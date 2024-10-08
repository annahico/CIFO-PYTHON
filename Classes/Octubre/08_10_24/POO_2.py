# Ejercicio 2
# Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo


class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def __str__(self) -> str:
        return f"El área del rectángulo es: {self.area()}"


r = Rectangulo(8, 25)
print(r.area())
