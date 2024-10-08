# Ejercicio 6
# Escribe una clase de Python, y define dos métodos que devuelvan el área del cuadrado y el perímetro.


# Definición de la clase Cuadrado
class Cuadrado:
    def __init__(self, lado):
        # Constructor que inicializa el lado del cuadrado
        self.lado = lado

    def area(self):
        # Método para calcular el área del cuadrado
        return self.lado ** 2

    def perimetro(self):
        # Método para calcular el perímetro del cuadrado
        return 4 * self.lado

    def __str__(self):
        # Método para mostrar una representación en string del objeto
        return f"Cuadrado de lado {self.lado}"


# Crear una instancia de la clase Cuadrado
lado = 5  # Puedes cambiar el valor del lado aquí
c = Cuadrado(lado)

# Imprimir los resultados
print(f"El área del cuadrado es: {c.area()}")
print(f"El perímetro del cuadrado es: {c.perimetro()}")
