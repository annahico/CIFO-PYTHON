# Implementar un programa que sol·liciti números a l'usuari –entrats un per un- fins que ingressi el zero. Després d’introduir cada número es mostrarà el seu factorial.
# Al finalitzar es mostrarà la quantitat total de números llegits.
# Utilitzar una o més funcions, segons sigui necessari.


def factorial(n):
    # Funció que calcula el factorial d'un número n.
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    # unció principal del programa.
    count = 0  # Contador per a la quantitat total de números llegits

    while True:
        # Sol·licitar un número a l'usuari
        num = int(input("Introdueix un número (0 per acabar): "))

        # Comprovem si el número és zero per acabar
        if num == 0:
            break

        # Calcular i mostrar el factorial del número
        fact = factorial(num)
        print(f"El factorial de {num} és {fact}.")

        # Incrementar el contador de números llegits
        count += 1

    # Mostrar la quantitat total de números llegits
    print(f"Has introduït un total de {count} números.")


# Executar el programa
main()
