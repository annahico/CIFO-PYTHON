# Escriu una funció de Python que trobi el màxim de tres números. No es pot
# utilitzar la funció max.

# def maxim(llista)
# ..................
# ..................
# ..................
# return ...........

# Per exemple,
# print(maxim([7,3,8]) imprimirà a la pantalla el número 8 que és el màxim dels tres números.

def maxim(llista):
    # Funció que troba el màxim de tres números.
    # Suposem que la llista conté exactament tres elements
    a, b, c = llista[0], llista[1], llista[2]
    # Inicialitzem el màxim amb el primer número
    max_num = a
    # Compara el màxim amb el segon número
    if b > max_num:
        max_num = b
    # Compara el màxim amb el tercer número
    if c > max_num:
        max_num = c
    return max_num


print(maxim([7, 3, 8]))  # Imprimirà 8
