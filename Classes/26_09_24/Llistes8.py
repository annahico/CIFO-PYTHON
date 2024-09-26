# 8. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb els elements en posició parell.

def posicio_parell_llista(llista): # defineixo la funció
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 == 0: #  El codi comprova si I és un nombre parell. utilitza l'operador de mòdul (%), que retorna el residu de dividir i per 2. Si el residu és zero (== 0), vol dir que i és parell, i la condició es compleix.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    
    return llista_resultat

llista1 = [4,3,2,1,8] # NO son els números parells, es LA POSICIÓ (0, 2, 4, 6, etc)
llista2 = [5,4,3,2,1] # NO son els números parells, es LA POSICIÓ (0, 2, 4, 6, etc)

print(posicio_parell_llista(llista1))
print(posicio_parell_llista(llista2))









