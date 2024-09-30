def nofirst_llista(llista):
    nolast = []
    for cadena in llista:
        nolast.append(cadena[1:])  # Afegeix la cadena sense el primer caràcter
    return nolast


llista = ['hola', 'com', 'estas']
print(nofirst_llista(llista))


# LIST COMPREHENSION

def nolast_llista2(llista):
    return [cadena[1:len(cadena)-1] for cadena in llista]


llista = ['hola', 'com', 'estas']
print(nofirst_llista(llista))
