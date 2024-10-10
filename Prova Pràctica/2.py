# Implementar un programa que sol·liciti números a l'usuari –entrats un per un- fins que ingressi el zero.
# Al final el programa mostrarà cada número i al costat la suma dels seus dígits.
# El zero no cal presentar-lo ( El programa contindrà una funció que realitzarà i retornarà la suma dels dígits d’un número).

# NOTA. El programa va demanant cada número per separat fins que en una de les entrades escrivim un zero.
# En aquest moment ens presentarà el resultat final tal com se sol·licita a l’enunciat.

# Per exemple, # Si introduïm 123 i després 25 abans del 0 – cada número en un input diferent, el resultat serà:
# 123 6
# 25 7


def suma_digits(num):
    # Funció que calcula la suma dels dígits d'un número.
    return sum(int(digit) for digit in str(num))


def main():
    # Funció principal del programa.
    numeros = []
    while True:
        # Sol·licitar un número a l'usuari
        num = int(input("Introdueix un número (0 per acabar): "))
        # Comprovem si el número és zero per acabar
        if num == 0:
            break
        # Afegim el número a la llista
        numeros.append(num)
    # Mostrar el resultat final
    for numero in numeros:
        suma = suma_digits(numero)
        print(f"{numero} {suma}")


# Executar el programa
main()
