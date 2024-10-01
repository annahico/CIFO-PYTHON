# 13. Multiplicar dos sencers en base a sumes successives

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
resultado = 0
contador = 0

while contador < abs(b):
    resultado += abs(a)
    contador += 1

# Ajustar signo según los números
if (a < 0 and b > 0) or (a > 0 and b < 0):
    resultado = -resultado

print(f"El resultado de {a} * {b} es: {resultado}")
