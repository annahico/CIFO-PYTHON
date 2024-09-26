# 12. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes en minúscules.

def minus_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append((str(llista[i].lower()))) # funció de cadenes, hem de convertir la llista i el I en cadena
    return llista_resultat

llista = ['HOLA','COM','ESTAS']

print(minus_llista(llista))