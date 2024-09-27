# 17. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició senar.

def parelles(llista): # defineixo la funció
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 != 0: #  El  codi recorre cada element de la llista llista I verifica si és senar (i % 2 != 0), és a dir, si no és divisible per 2.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    return llista_resultat

llista = ['hola', 'com', 'estas']

print(parelles(llista))


# -----------------------------------------------------------------------------------------------------


def parelles(x):
    pass

original = ['hola', 'com', 'estas']
result = parelles(original)
print (f"La cadena original és {original} i la modificada {result}")

# l'element que es troba a la posició 0 és 'hola' i es reconeix com original[0]
# l'element que es troba a la posició 1 és 'com' i es reconeix com original[1]
# l'element que es troba a la posició 2 es 'estàs' i es reconeix com original[2]