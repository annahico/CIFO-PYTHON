def longitud_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append(len(str(llista[i])))
    return llista_resultat


llista = ['hola', 'com', 'estas']

print(longitud_llista(llista))


# LIST COMPREHENSION

def longitud_llista(llista):
    return [len(str(llista[i])) for i in range(len(llista))]


llista = ['hola', 'com', 'estas']

print(longitud_llista(llista))
