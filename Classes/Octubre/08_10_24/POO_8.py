# Ejercicio 8
# 1 - Crear una clase Cálculos con un constructor por defecto (sin parámetros) que permita realizar varios cálculos sobre números enteros.
# 2 - Crear un método llamado factorial() que permita calcular el factorial de un entero.
# 3  -  Crear  un  método  llamado  suma()  que  permita  calcular  la  suma  de  los  primeros  n  enteros 1 + 2 + 3 + .. + n.
# 4 - Crea un método llamado testPrimo() en la clase Cálculo para comprobar si un número es primo. El resultado será True o False.
# 5 - Crear un método llamado testPrimos() que permita comprobar si dos números son primos entre sí.
# 6 -  Cree  un  método  tablaMult()  que  cree  y  muestre  la  tabla  de  multiplicación  de  un  número  entero  dado.  A  continuación,  cree  un  método  allTablesMult()  para  mostrar  todas las tablas de multiplicación de enteros 1, 2, 3, ..., 9.
# 7 - Crear un método listDiv() que obtenga todos los divisores de un entero dado en una nueva lista llamada Ldiv.


class Calculos:
    def __init__(self) -> None:
        pass

    # Método para calcular el factorial de un número
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    # Método para calcular la suma de los primeros n enteros
    def suma(self, n: int) -> int:
        return sum(range(1, n + 1))

    # Método para comprobar si un número es primo
    def testPrimo(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Método para comprobar si dos números son primos entre sí (primos relativos)
    def testPrimos(self, a: int, b: int) -> bool:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return gcd(a, b) == 1

    # Método para mostrar la tabla de multiplicar de un número
    def tablaMult(self, n: int) -> None:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

    # Método para mostrar las tablas de multiplicar del 1 al 9
    def allTablesMult(self) -> None:
        for i in range(1, 10):
            print(f"\nTabla de multiplicar del {i}:")
            self.tablaMult(i)

    # Método para obtener los divisores de un número
    def listDiv(self, n: int) -> list:
        Ldiv = [i for i in range(1, n + 1) if n % i == 0]
        return Ldiv

    # Método __str__ para representar la clase en forma de cadena
    def __str__(self) -> str:
        return "Clase para realizar cálculos diversos"


# Ejemplo de uso
c = Calculos()

# Pruebas
print("Factorial de 5:", c.factorial(5))         # Output: 120
print("Suma de los primeros 5 enteros:", c.suma(5))  # Output: 15
print("¿Es 7 un número primo?:", c.testPrimo(7))    # Output: True
print("¿Son 15 y 28 primos entre sí?:", c.testPrimos(15, 28))  # Output: True

print("\nTabla de multiplicar del 7:")
c.tablaMult(7)

print("\nTablas de multiplicar del 1 al 9:")
c.allTablesMult()

# Output: [1, 2, 4, 7, 14, 28]
print("\nDivisores de 28:", c.listDiv(28))
