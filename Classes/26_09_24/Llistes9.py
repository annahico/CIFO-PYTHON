# 9. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb els elements en posició senar.

def posicio_senar_llista(llista): # defineixo la funció
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 != 0: #  El  codi recorre cada element de la llista llista I verifica si és senar (i % 2 != 0), és a dir, si no és divisible per 2.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    
    return llista_resultat

llista1 = [4,3,2,1,8] 
llista2 = [5,4,3,2,1] 

print(posicio_senar_llista(llista1))
print(posicio_senar_llista(llista2))


# ---------------------------------------------------------------------------------------------------

def imparell(l):
    resultat = []
    for posicio in range(1,len(l),2):
        resultat.append(l[posicio])
    return resultat

original = [-11,13,1,25]
imparells = imparell(original)
print(imparells)
print (original)