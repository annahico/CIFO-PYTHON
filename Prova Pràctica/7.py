# Escriu una funció a Python per comprovar si un número és perfecte o no.
# Segons la Wikipedia : En teoria de números, un nombre perfecte és un nombre sencer
# positiu que és igual a la suma dels seus divisors positius propis, és a dir, la suma
# dels seus divisors positius excloent el mateix número (també conegut com la seva suma alíquota).
# Un nombre perfecte és un nombre que és la meitat de la suma de tots els seus divisors positius (inclòs ell mateix).

# Exemple:
# El primer número perfecte és el 6, perquè 1, 2 i 3 són els seus divisors positius propis, i 1 + 2 + 3 = 6.
# De forma equivalent, el número 6 és igual a la meitat de la suma de tots els seus divisors positius: ( 1 + 2 + 3 + 6 ) / 2 = 6.
# El següent número perfecte és 28 = 1 + 2 + 4 + 7 + 14.
# El segueixen els números perfectes 496 i 8128.

# def perfecte(numero):
# ..................
# ..................
# ..................
# return ...........

# Per exemple,
# print(perfecte(28)) imprimirà a la pantalla True
# print(perfecte(26)) imprimirà a la pantalla False


def perfecte(numero):
    # Comprova si un número és perfecte.
    if numero < 1:
        return False  # Els números positius són requerits
    suma_divisors = 0
    # Calcular la suma dels divisors propis
    for i in range(1, numero):
        if numero % i == 0:  # Comprovem si 'i' és un divisor de 'numero'
            suma_divisors += i
    # Comprovem si la suma dels divisors és igual al número
    return suma_divisors == numero


print(perfecte(28))  # Imprimirà True
print(perfecte(26))  # Imprimirà False
