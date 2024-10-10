# Escriu una funció de Python que accepta una string i calcula el número de
# majúscules i minúscules que apareixen a la cadena.
# La funció retornarà una llista Amb dos elements el número de majúscules i minúscules.

# def aparicions(cadena):
# ..................
# ..................
# ..................
# return ...........

# Per exemple,

# 4

# print(aparicions(“Hola Caracola, a tu bola”)) imprimirà a la pantalla la llista # [2,17] perquè a la cadena hi ha 2 majúscules i 17 minúscules.
# NOTA. En aquesta versió no cal escriure les cadenes amb accents.
# Els espais o altres caràcters no es consideren majúscules o minúscules.


def aparicions(cadena):
    # Calcula el número de majúscules i minúscules en una cadena.
    majuscules = 0
    minuscules = 0

    for caracter in cadena:
        if caracter.isupper():  # Comprovem si el caràcter és majúscula
            majuscules += 1
        elif caracter.islower():  # Comprovem si el caràcter és minúscula
            minuscules += 1
    return [majuscules, minuscules]


resultat = aparicions("Hola Caracola, a tu bola")
print(resultat)  # Imprimirà [2, 17]
