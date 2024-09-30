# CSV = FES UN CODI INCREMENTI EN 1 TOTS ELS NÚMEROS DE LA SEGÜENTS LLISTES

# matriu = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]
# |
# codi
# |
# |
# resultat = [[3, 6, 11], [7, 8, 10], [5, 6, 11]]


# VERSIÓ 1

def incremento(llista):
    resultado = []  # valor de columna
    for columna in llista:
        resultado.append(columna + 1)

    return resultado


matriu = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]
resultat = []
for fila in matriu:  # valor de fila
    resultat.append(incremento(fila))
    incremento(fila)

print(resultat)

# VERSIÓ 2

matriu = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]
for element in matriu:  # element es [2,5,10]etc... de la MATRIU
    # analitzes totes les POSICIONS de cada ELEMENT(0,1,2, etc)
    for pos in range(len(element)):
        # analitzes la pocisio de cada element i sumes +1 a cada element
        element[pos] += 1
print(matriu)


# VERSIÓ 3 (LIST COMPREHENSION) NOMÉS ES POT UTILITZAR EN LES LLISTES

def incremento(l):  # s'ha comprimit la primera part de la versió 1

    return [element + 1 for element in l]


matriu = [[2, 5, 10], [6, 7, 9], [4, 5, 10]]

# s'ha comprimit la segona part de la versió 1
resultat = [incremento(fila) for fila in matriu]

print(resultat)
