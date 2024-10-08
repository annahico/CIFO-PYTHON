# Ejercicio 7

# Se requiere un programa que modele una cuenta bancaria que posee los siguientes atributos:

# - Nombres del titular
# - Apellidos del titular
# - Numero de la cuenta bancaria
# - Tipo de cuenta: puede ser una cuenta de ahorros o una cuenta
# - Saldo de la cuenta

# Se debe definir un constructor que inicialice los atributos de la clase.
# Cuando se crea una cuenta bancaria, su saldo inicial tiene un valor de cero.
# En una determinada cuenta bancaria se puede:
# - Imprimir por pantalla los valores de los atributos de una cuenta bancaria
# - Consultar el saldo de una cuenta bancaria
# - Consignar un determinado valor en la cuenta bancaria, actualizando el saldo correspondiente
# - Retirar un determinado valor de la cuenta bancaria, actualizando el saldo correspondiente. Es necesario tener en cuenta que no se puede realizar el retiro si el valor solicitado supera el saldo actual de la cuenta.


class Cuenta:
    def __init__(self, nombres, apellidos, numero, tipo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0  # El saldo inicial es 0

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Consignación de {
                  valor} realizada. Saldo actual: {self.saldo}")
        else:
            print("El valor a consignar debe ser positivo.")

    def retirar(self, valor):
        if valor > self.saldo:
            print(f"No es posible retirar {
                  valor}. Saldo insuficiente: {self.saldo}")
        elif valor > 0:
            self.saldo -= valor
            print(f"Retiro de {valor} realizado. Saldo actual: {self.saldo}")
        else:
            print("El valor a retirar debe ser positivo.")

    def __str__(self):
        return f"Cuenta {self.tipo} - Titular: {self.nombres} {self.apellidos}, Número: {self.numero}, Saldo: {self.saldo}"


# Ejemplo de uso
cuenta1 = Cuenta("Juan", "Pérez", "123456789", "Ahorros")

# Imprimir detalles de la cuenta
print(cuenta1)

# Consultar saldo
print("Saldo actual:", cuenta1.consultar_saldo())

# Consignar dinero
cuenta1.consignar(500)

# Intentar retirar más de lo que hay en la cuenta
cuenta1.retirar(600)

# Retirar una cantidad válida
cuenta1.retirar(200)


# ---------------------------------------------------------------------------------------------------

class CCC:
    def __init__(self, nom, cognom, nCCC, tipo) -> None:
        self.nom = nom
        self.cognom = cognom
        self.nCCC = nCCC
        self.tipo = tipo
        self.saldo = 0

    def mostrar_saldo(self):
        print(f"El saldo actual és: {self.saldo}")

    def __str__(self) -> str:
        return (f"El nom i cognoms de la persona titular és: {self.nom} {self.cognom}\n"
                f"El número de compte és: {self.nCCC}\n"
                f"El compte és del tipus: {self.tipo}\n"
                f"La persona titular té un saldo de {self.saldo}\n")


c = CCC("Cristian", "Compi Esquerra", 1234567890, "credit")

print(c)
c.mostrar_saldo()
