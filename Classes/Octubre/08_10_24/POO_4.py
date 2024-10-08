# Ejercicio 4
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# • mostrar(): Muestra los datos de la persona.
# • esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:
    def __init__(self, nombre='', edad=0, dni='') -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setters y Getters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres")

    # Método para mostrar los datos de la persona
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    # Método para verificar si es mayor de edad
    def esMayorDeEdad(self):
        return self.edad >= 18

    # Método __str__ para imprimir la información de la persona
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"


# Ejemplo de uso
p = Persona()
p.set_nombre("Juan")
p.set_edad(20)
p.set_dni("12345678A")
print(p.mostrar())  # Mostra els atributs
print(p.esMayorDeEdad())  # Verifica si és major de 18
