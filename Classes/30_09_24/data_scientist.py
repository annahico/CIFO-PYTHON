# CSV = FES UN CODI INCREMENTI EN 1 TOTS ELS NÚMEROS DE LA SEGÜENTS LLISTES

# llista = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]
# |
# codi
# |
# |
# resultat = [[3, 6, 11], [7, 8, 10], [5, 6, 11]]


def incremento(lista):
    resultado = []  # valor de columna
    for columna in lista:
        resultado.append(columna + 1)

    return resultado


matriu = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]
resultat = []
for fila in matriu:  # valor de fila
    resultat.append(incremento(fila))
    incremento(fila)

print(resultat)
