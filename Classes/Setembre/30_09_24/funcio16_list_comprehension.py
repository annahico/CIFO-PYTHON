def parelles(llista):  # defineixo la funció
    llista_resultat = []
    for i in range(len(llista)):  # El codi recorre cada índex de la llista llista (i= index)
        # El codi comprova si I és un nombre parell. utilitza l'operador de mòdul (%), que retorna el residu de dividir i per 2. Si el residu és zero (== 0), vol dir que i és parell, i la condició es compleix.
        if i % 2 == 0:
            # Afegeix l'element llista[i] a llista_resultat.
            llista_resultat.append(llista[i])
    return llista_resultat


llista = ['hola', 'com', 'estas']

print(parelles(llista))


# LIST COMPREHENSION

def parelles(llista):
    return [llista[pos] for pos in range(len(llista)) if pos % 2 == 0]


llista = ['hola', 'com', 'estas']

print(parelles(llista))
