# 16. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició parell.

def parelles(llista): # defineixo la funció
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 == 0: #  El codi comprova si I és un nombre parell. utilitza l'operador de mòdul (%), que retorna el residu de dividir i per 2. Si el residu és zero (== 0), vol dir que i és parell, i la condició es compleix.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    return llista_resultat

llista = ['hola', 'com', 'estas']

print(parelles(llista))
