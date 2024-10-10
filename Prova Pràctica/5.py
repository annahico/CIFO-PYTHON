# Escriu una funció de Python que comprovi si un número cau en un rang donat.

# def dinsrang(numero, rang1, rang2):
# ..................
# ..................
# ..................
# return ...........

# Per exemple,
# print(dinsrang(3,2,5)) imprimirà True, ja que 3 es troba entre els números 2 i 5.
# print(dinsrang(5,2,3)) imprimirà False, ja que 5 no es troba entre els números 2 i 3.


def dinsrang(numero, rang1, rang2):
    # Comprova si un número cau dins d'un rang donat.
    # Assegurem que rang1 sigui el menor i rang2 el major
    if rang1 > rang2:
        rang1, rang2 = rang2, rang1
    # Comprovem si el número està dins del rang
    return rang1 <= numero <= rang2


print(dinsrang(3, 2, 5))  # Imprimirà True
print(dinsrang(5, 2, 3))  # Imprimirà False
