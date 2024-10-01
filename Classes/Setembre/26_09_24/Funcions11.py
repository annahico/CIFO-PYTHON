# 11. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb la longitud de cadascuna de les cadenes que formen la llista.


def longitud_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append(len(str(llista[i])))
    return llista_resultat

llista = ['hola','com','estas']

print(longitud_llista(llista))



# CHAT GPT:

def longitud_llista(llista):
    return [len(cadena) for cadena in llista]

llista = ['hola', 'com', 'estas']
print(longitud_llista(llista))
