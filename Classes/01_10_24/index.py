llistadellistes = [['hola', 'pepe', 'com', 'estas'],
                   ['la', 'farola', 'de', 'laredo']]

for llista in llistadellistes:
    for element in llista:  # ELEMENT = cadascuna de les paraules
        print(element)

# --------------------------------------------------------------------------------------------------

# RANGE =  longitud de les paraules. POS = posició de la lletra de cada paraula
for llista in llistadellistes:
    for element in llista:
        print(element)
for pos in range(len(llista)):
    llista[pos] = llista[pos][1:]
print(llistadellistes)

# --------------------------------------------------------------------------------------------------

for llista in llistadellistes:
    for pos in range(len(llista)):
        llista[pos] = llista[pos][1:]
        print(llistadellistes)

# --------------------------------------------------------------------------------------------------


def nofirst(lista):  # agafa una llista de cadenes com a parametre i li treu a cada cadena el primer caracter
    resultat = []
    for element in lista:
        resultat.append(element[1:])
    return resultat


print(nofirst(['hola', 'pepe', 'com', 'estas']))

llistadellistes = [['hola', 'pepe', 'com', 'estas'],
                   ['la', 'farola', 'de', 'laredo']]
resultat = []
for llista in llistadellistes:
    resultat.append(nofirst(llista))
print(resultat)
