def mayus_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        # funció de cadenes, hem de convertir la llista i el I en cadena
        llista_resultat.append((str(llista[i].upper())))
    return llista_resultat


llista = ['hola', 'com', 'estas']

print(mayus_llista(llista))


# LIST COMPREHENSION

def mayus_llista(llista):
    return [element.upper() for element in llista]


llista = ['HOLA', 'COM', 'ESTAS']

print(mayus_llista(llista))
