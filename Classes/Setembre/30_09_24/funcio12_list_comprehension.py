def minus_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        # funció de cadenes, hem de convertir la llista i el I en cadena
        llista_resultat.append((str(llista[i].lower())))
    return llista_resultat


llista = ['HOLA', 'COM', 'ESTAS']

print(minus_llista(llista))


# LIST COMPREHENSION

def minus_llista(llista):
    return [element.lower() for element in llista]


llista = ['HOLA', 'COM', 'ESTAS']

print(minus_llista(llista))
