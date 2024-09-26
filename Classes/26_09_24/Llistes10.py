# 10. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb el número de dígits de cada element.

def digits_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append(len(str(llista[i]))) # afegeixo la longitut (indicant que es un string) de la llista i quants digits hi han en cada element (I)

    return llista_resultat

llista2 = [5,4,3,2,1]
llista1 = [4,3,2,1,8]

print(digits_llista(llista1))
print(digits_llista(llista2))