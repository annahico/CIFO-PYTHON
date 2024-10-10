# Implementar un programa que sol·liciti números a l'usuari –entrats un per un- fins que ingressi el zero. Després d’introduir cada número es mostrarà el seu factorial.
# Al finalitzar es mostrarà la quantitat total de números llegits.
# Utilitzar una o més funcions, segons sigui necessari.


def factorial(n):
    # Calcula el factorial d'un número n.
    if n < 0:
        return None  # El factorial no està definit per a números negatius
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    # Funció principal que gestiona la introducció de números i la seva processament.
    count = 0  # Contador de números llegits

    while True:
        # Sol·licitem un número a l'usuari
        number = int(input("Introdueix un número (0 per acabar): "))

        # Si el número és 0, acabem el bucle
        if number == 0:
            break

        # Incrementem el contador
        count += 1

        # Calculem el factorial del número
        fact = factorial(number)

        # Mostrem el resultat
        print(f"El factorial de {number} és: {fact}")

    # Mostrem la quantitat total de números llegits
    print(f"Total de números llegits: {count}")


# Executem el programa
if __name__ == "__main__":
    main()
