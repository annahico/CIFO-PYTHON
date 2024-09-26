# 18. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes sense l'últim caràcter

# def nolast_llista(llista): #FUNCIÓ
#     for posicio in range(len(llista)):
#         llista[posicio] = llista[posicio][0:len(llista[posicio])-1] # cada element de la llista és actualitzat per la seva versió sense l'últim caràcter.
#     return (llista) # 

# llista = ['hola', 'com', 'estas']
# print(nolast_llista(llista)) 


def nolast_llista2(llista):
    nolast = []
    for cadena in llista:
        nolast.append(cadena[0:len(cadena)-1]) # recorre els elements de cada cadena i elimina l'últim caracter de cada cadena de la llista
    return (nolast)

llista = ['hola', 'com', 'estas']
print(nolast_llista2(llista))